import type { NextPage } from 'next'
import Head from 'next/head'
import useSWR from 'swr'
import { useSWRConfig } from 'swr'

import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import TextField from '@mui/material/TextField';
import { Button } from '@mui/material';
import { useState } from 'react';


const columns: GridColDef[] = [
  { field: 'id', headerName: 'ID', width: 90 },
  {
    field: 'name',
    headerName: 'Name',
    width: 150,
    editable: false,
  },
  {
    field: 'created_at',
    headerName: 'Created at',
    width: 200,
    editable: false,
  },
  {
    field: 'updated_at',
    headerName: 'Updated at',
    type: 'number',
    width: 200,
    editable: false,
  },
];

type User = {
  id: number
  name: string
  created_at: string
  updated_at: string
}

const Home: NextPage = () => {
  const fetcher = (url: string) => fetch(url).then(r => r.json())
  const { data, error } = useSWR<User[]>('/show', fetcher)

  const [id, setId] = useState<number>(0)
  const [name, setName] = useState<string>("")

  const { mutate } = useSWRConfig();

  const onAdd = async () => {
    console.log("Add", { id }, { name })
    const d = [
      {
        "id": id,
        "name": name,
        // "created_at": "2022-12-10T14:59:33.389762",
        // "updated_at": "2022-12-10T15:00:09.941Z"
      }
    ]
    console.log(d)
    const res = await fetch("/add", {
      method: 'POST', headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(d)
    })
    const json = await res.json()
    console.log(json)
    mutate('/show')
  }

  const onDelete = async () => {
    console.log("Delete", { id }, { name })
    const d = [id]
    const res = await fetch("/delete", {
      method: 'DELETE', headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(d)
    })
    const json = await res.json()
    console.log(json)
    mutate('/show')
  }


  // if (error) return <div>failed to load</div>
  // if (!data) return <div>loading...</div>

  console.log(data)
  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>


      <TextField id="outlined-basic" label="Name" variant="outlined" onChange={(event) => { setName(event.target.value) }} />
      <TextField id="outlined-basic" label="ID" variant="outlined" onChange={(event) => { setId(Number(event.target.value)) }} />

      <Button variant="contained" color="success" onClick={onAdd}>ADD</Button>
      <Button variant="contained" color="error" onClick={onDelete}>DELETE</Button>

      <Box sx={{ height: 400, width: '100%' }}>
        <DataGrid
          rows={data?.length === undefined ? [] : data}
          columns={columns}
          pageSize={5}
          rowsPerPageOptions={[5]}
          checkboxSelection
          disableSelectionOnClick
          experimentalFeatures={{ newEditingApi: true }}
        />
      </Box>
    </div>
  )
}

export default Home

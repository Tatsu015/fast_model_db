import type { NextPage } from 'next'
import Head from 'next/head'
import useSWR from 'swr'

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

const rows = [
  {
    "id": 1,
    "created_at": "2022-12-10T07:42:45",
    "updated_at": "2022-12-10T07:43:40",
    "name": "bbbb"
  },
  {
    "id": 2,
    "created_at": "2022-12-10T07:42:45",
    "updated_at": "2022-12-10T07:43:40",
    "name": "aaaaa"
  }
]

const Home: NextPage = () => {
  const fetcher = (url: string) => fetch(url).then(r => r.json())
  const { data, error } = useSWR('/show', fetcher)

  const [id, setId] = useState<number>(0)
  const [name, setName] = useState<string>("")

  const onAdd = () => {
    console.log("Add", { id }, { name })
  }
  const onDelete = () => {
    console.log("Delete", { id }, { name })
  }


  // if (error) return <div>failed to load</div>
  // if (!data) return <div>loading...</div>

  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>


      <TextField id="outlined-basic" label="ID" variant="outlined" onChange={(event) => { setId(Number(event.target.value)) }} />
      <TextField id="outlined-basic" label="Name" variant="outlined" onChange={(event) => { setName(event.target.value) }} />

      <Button variant="contained" color="success" onClick={onAdd}>ADD</Button>
      <Button variant="contained" color="error" onClick={onDelete}>DELETE</Button>

      <Box sx={{ height: 400, width: '100%' }}>
        <DataGrid
          rows={rows}
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

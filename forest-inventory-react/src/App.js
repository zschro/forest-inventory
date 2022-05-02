import Pagination from '@mui/material/Pagination';
import Stack from '@mui/material/Stack';
import ForestCard from './ForestCard';
import { useEffect, useState } from 'react'
import axios from "axios";
import './App.css';
import { Container } from '@mui/material';

function App() {
  const [loading, setLoading] = useState(true);
  const [forestData, setForestData] = useState(null);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const handleChange = (event, value) => {
    setPage(value);
    setLoading(true);
    fetchData(value);
  };

  const fetchData = async (inputPage = null) =>{
    try {
      const {data: response} = await axios.get('/forests?page=' + (inputPage ?? page));
      setForestData(response.forests);
      setTotalPages(response.totalPages);
    } catch (error) {
      console.error(error.message);
    }
    setLoading(false);
  }

  useEffect(() => {
      setLoading(true);
      fetchData();
    }, []);

  return (
    <div className="App">
      <Container>
        {loading && <div>Loading</div>}
        {!loading &&
          <Stack direction="row" spacing={3} sx={{flexWrap:"wrap"}} justifyContent="space-between" alignItems="center">
            {forestData.map(forest => (<ForestCard forest={forest}/>))}
          </Stack>
        }
        <Pagination count={totalPages} page={page} onChange={handleChange} />
      </Container>
    </div>
  );
}

export default App;

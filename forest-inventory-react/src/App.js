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

    useEffect(() => {
      const fetchData = async () =>{
        setLoading(true);
        try {
          const {data: response} = await axios.get('/forests');
          setForestData(response);
        } catch (error) {
          console.error(error.message);
        }
        setLoading(false);
      }
  
      fetchData();
    }, []);

  return (
    <div className="App">
      <Container>
        {loading && <div>Loading</div>}
        {!loading &&
          <Stack direction="row" spacing={2}>
            {forestData.map(forest => (<ForestCard forest={forest}/>))}
          </Stack>
        }
        <Pagination count={10} />
      </Container>
    </div>
  );
}

export default App;

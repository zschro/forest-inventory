import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import Collapse from '@mui/material/Collapse';

export default function ActionAreaCard() {
    const [expanded, setExpanded] = React.useState(false);
    const handleExpandClick = () => {
        setExpanded(!expanded);
      };
    return (
        <Card sx={{ maxWidth: 345 }}>
        <CardActionArea onClick={handleExpandClick}>
            <CardMedia
            component="img"
            height="140"
            image="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Amazonia.jpg/272px-Amazonia.jpg"
            alt="Amazon rainforest on the Urubu River"
            />
            <CardContent>
            <Typography gutterBottom variant="h5" component="div">
                Amazon Rain Forest
            </Typography>
            </CardContent>
        </CardActionArea>
        <Collapse in={expanded} timeout="auto" unmountOnExit>
            <CardContent>
            <Typography variant="body2" color="text.secondary">
            The Amazon rainforest, alternatively, the Amazon jungle or Amazonia, is a moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 km2 (2,700,000 sq mi), of which 5,500,000 km2 (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations and 3,344 formally acknowledged indigenous territories.
    The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Bolivia, Ecuador, French Guiana, Guyana, Suriname, and Venezuela. Four nations have "Amazonas" as the name of one of their first-level administrative regions, and France uses the name "Guiana Amazonian Park" for its rainforest protected area. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species.
    More than 30 million people of 350 different ethnic groups live in the Amazon, which are subdivided into 9 different national political systems and 3,344 formally acknowledged indigenous territories. Indigenous peoples make up 9% of the total population with 60 of the groups remaining largely isolated.
            </Typography>
            </CardContent>
        </Collapse>
        </Card>
    );
}
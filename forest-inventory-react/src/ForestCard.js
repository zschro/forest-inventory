import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import Collapse from '@mui/material/Collapse';

export default function ActionAreaCard(props) {
    const [expanded, setExpanded] = React.useState(false);
    const handleExpandClick = () => {
        setExpanded(!expanded);
      };
    const forest = props.forest;
    return (
        <Card sx={{ maxWidth: 345 }}>
        <CardActionArea onClick={handleExpandClick}>
            <CardMedia
            component="img"
            height="140"
            image={forest.imgUrl}
            />
            <CardContent>
            <Typography gutterBottom variant="h5" component="div">
                {forest.name}
            </Typography>
            </CardContent>
        </CardActionArea>
        <Collapse in={expanded} timeout="auto" unmountOnExit>
            <CardContent>
            <Typography variant="body2" color="text.secondary">
                {forest.description}
            </Typography>
            </CardContent>
        </Collapse>
        </Card>
    );
}
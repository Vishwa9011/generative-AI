import { useState } from 'react'
import { Table, Thead, Tbody, Tr, Th, Td, TableCaption, TableContainer, Button, Popover, PopoverTrigger, PopoverContent, PopoverArrow, PopoverHeader, PopoverCloseButton, PopoverBody, Input, Select, useDisclosure, Box, PopoverFooter, ButtonGroup, } from '@chakra-ui/react'
import { dish } from '../../constants/constants';
import axios from 'axios';
import { v4 as uuid } from 'uuid';


const ListOrders = ({ dishes, editData }: { dishes: dish[], editData(dish: dish): void }) => {

     return (
          <>
               <TableContainer>
                    <Table variant='simple'>
                         <TableCaption>Imperial to metric conversion factors</TableCaption>
                         <Thead>
                              <Tr>
                                   <Th>S.no</Th>
                                   <Th>Dish ID</Th>
                                   <Th>Dish Name</Th>
                                   <Th>Dish Price</Th>
                                   <Th>Dish Stock</Th>
                                   <Th>Order Now</Th>
                                   <Th>Edit</Th>
                                   <Th>Delete</Th>
                              </Tr>
                         </Thead>
                         <Tbody>
                              {dishes && dishes.length &&
                                   dishes.map((dish, i) => (
                                        <Tr key={i}>
                                             <Td>{i + 1}</Td>
                                             <Td>{dish?.id}</Td>
                                             <Td>{dish.name}</Td>
                                             <Td>{dish.price}</Td>
                                             <Td>{dish.stock}</Td>
                                             <Td>
                                                  <Button onClick={() => editData(dish)}>Edit</Button>
                                             </Td>
                                             <Td>
                                                  <OrderNowButton data={dish} />
                                             </Td>
                                             <Td>
                                                  <Button>Delete</Button>
                                             </Td>
                                        </Tr>
                                   ))}
                         </Tbody>
                    </Table>
               </TableContainer>
          </>
     )
}

export default ListOrders


function OrderNowButton({ data }: { data: dish }) {
     const [name, setName] = useState('')
     const [quantity, setQuantity] = useState(0)
     const { onOpen, onClose, isOpen } = useDisclosure()

     const createOrder = () => {

          if (!name || !quantity) {
               return alert("Please fill the fieilds")
          }
          if (quantity > data.stock) {
               return alert(`We have only ${quantity} stock left.`)
          }
          axios.post(`/update/${data?.id}`, { ...data, stock: data['stock'] - quantity })
               .then(res => {
                    console.log('res: ', res);
                    axios.post('/neworder', {
                         id: uuid(), name, quantity, status: "recieved",
                         dish: { id: data.id, name: data.name, price: data.price }
                    })
                         .then((res) => {
                              console.log('res: ', res);
                              onClose()
                         })
                         .catch((err) => {
                              console.log('err: ', err);
                         })
               })
     }

     return (
          <Popover
               isLazy
               isOpen={isOpen}
               onOpen={onOpen}
               onClose={onClose}
               placement='auto'
               closeOnBlur={false}
          >
               <PopoverTrigger>
                    <Button>Order Now</Button>
               </PopoverTrigger>
               <PopoverContent>
                    <PopoverHeader fontWeight='semibold'>Book your order</PopoverHeader>
                    <PopoverArrow />
                    <PopoverCloseButton />
                    <PopoverBody>
                         <Box display='grid' gap={'1rem'}>
                              <Input value={name} placeholder='Enter your name' onChange={(e) => setName(e.target.value)} />
                              <Select value={quantity} onChange={(e) => setQuantity(+e.target.value || 0)}>
                                   <option value="0">Choose the quantity</option>
                                   <option value="1">1</option>
                                   <option value="2">2</option>
                                   <option value="3">3</option>
                                   <option value="4">4</option>
                                   <option value="5">5</option>
                                   <option value="6">6</option>
                              </Select>
                         </Box>
                    </PopoverBody>
                    <PopoverFooter display='flex' justifyContent='flex-end'>
                         <ButtonGroup size='sm'>
                              <Button variant='outline' onClick={onClose}>Cancel</Button>
                              <Button colorScheme='red' onClick={createOrder}>Order</Button>
                         </ButtonGroup>
                    </PopoverFooter>
               </PopoverContent>
          </Popover>
     )
}
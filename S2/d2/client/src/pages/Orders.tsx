import { useEffect, useState } from 'react'
import {
     Table, Thead, Tbody, Tfoot, Tr, Th, Td, TableCaption, TableContainer, Select,
} from '@chakra-ui/react'
import axios from 'axios'
export const Orders = () => {
     const [ordersData, setOrdersData] = useState([])

     const getOrdersData = () => {
          axios.get('/orders')
               .then(res => setOrdersData(res.data))
               .catch(err => console.log(err))
     }

     useEffect(() => {
          getOrdersData()
     }, [])

     return (
          <TableContainer>
               <Table variant='simple'>
                    <TableCaption>Imperial to metric conversion factors</TableCaption>
                    <Thead>
                         <Tr>
                              <Th>S.no</Th>
                              <Th>Order ID</Th>
                              <Th>Customer Name</Th>
                              <Th>Dish Name</Th>
                              <Th>Dish Price</Th>
                              <Th>Order Status</Th>
                              <Th>Change Order Status</Th>
                         </Tr>
                    </Thead>
                    <Tbody>
                         {ordersData && ordersData.length > 0 &&
                              ordersData.map((order: any, i) => (
                                   <Tr key={order?.id}>
                                        <Td>{i}</Td>
                                        <Td>{order?.id}</Td>
                                        <Td>{order?.name}</Td>
                                        <Td>{order?.dish?.name}</Td>
                                        <Td>{order?.dish?.price}</Td>
                                        <Td>{order?.status}</Td>
                                        <Td>
                                             <Select>
                                                  <option value="recieved">Recieved</option>
                                                  <option value="pending">Pending</option>
                                                  <option value="preparing">Preparing</option>
                                                  <option value="delivered">Delivered</option>
                                             </Select>
                                        </Td>
                                   </Tr>
                              ))}
                    </Tbody>
               </Table>
          </TableContainer>
     )
}

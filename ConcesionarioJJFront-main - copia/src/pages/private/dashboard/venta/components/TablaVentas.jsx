import React, { useEffect, useState } from "react";
import { getVentasData } from "../../../../../services/ventasService";
import { Column } from "primereact/column";
import { DataTableComponent } from "../../../../../components";
import { ToolbarVentas } from "./ToolbarVentas";
import { FacturaVentaPDF } from "../../../../../components/factura/FacturaVentaPDF";
import { PDFDownloadLink } from "@react-pdf/renderer";

export const TablaVentas = () => {
  const [ventas, setVentas] = useState([]);

  useEffect(() => {
    const getVentas = async () => {
      try {
        const response = await getVentasData();

        const dataVenta = response.map(venta => {
          return {
            ventaId: venta.ventaId,
            fecha: venta.fecha,
            usuarioVendedor: venta.vendedor_id?.username,
            idVendedor: venta.vendedor_id?.idUsuario,
            idCliente: venta.identificacion,
            nombreCliente: venta.nombreCliente + " " + venta.apellidoCliente, 
            sucursal: venta.sucursal?.nombre,
            metodoPago: venta.metodoPago,
          };
        });
        
        setVentas(dataVenta);
      } catch (error) {
        console.log(error);
      }
    };
    getVentas();
  }, []);

  const [TableComponent, dt] = DataTableComponent();

  const descargarFactura = rowData => {

    const venta = {
        idFactura: 1,
        fecha: "2021-10-09",
        idCliente: 1,
        nombreCliente: "Juan",
        apellidoCliente: "Perez",
        sucursal: "Sucursal 1",
        totalPagar: 100000,
        metodoPago: "Efectivo",
        detalleVenta: [
          {
            idDetalleVenta: 1,
            idCarro: 1,
            cantidad: 1,
            precio: 100000,
          },
        ],
      };

    return (
      <PDFDownloadLink document={<FacturaVentaPDF venta={venta} />} fileName="factura">
        <div className="flex justify-center cursor-pointer">
          <img
            className="w-10 h-10"
            src="data:image/png;base64,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"
            alt=""
          />
        </div>
      </PDFDownloadLink>
    );
  };

  return (
    <div className="bg-white rounded-md shadowContainer card p-6">
      <ToolbarVentas dt={dt} />

      <TableComponent data={ventas}>
        <Column header="Factura" body={descargarFactura} />
        <Column field="ventaId" header="ID" sortable filter />
        <Column field="fecha" header="Fecha" sortable filter />
        <Column field="usuarioVendedor" header="Vendedor" sortable filter />
        <Column field="idVendedor" header="ID Vendedor" sortable filter />
        <Column field="idCliente" header="ID Cliente" sortable filter />
        <Column field="nombreCliente" header="Cliente" sortable filter />
        <Column field="sucursal" header="Sucursal" sortable filter />
        <Column field="metodoPago" header="Metodo de pago" sortable filter />
      </TableComponent>
    </div>
  );
};

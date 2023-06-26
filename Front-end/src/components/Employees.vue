<script setup>
import axios from 'axios'
import { reactive, onMounted, ref, watch, createVNode } from 'vue';
import { useRouter } from 'vue-router';
import { Modal } from 'ant-design-vue';
import { ExclamationCircleOutlined } from '@ant-design/icons-vue';

const router = useRouter();

const data = reactive(
    {
        employees: [],
    });

const searchText = ref('')

onMounted(async () => {
    await axios.get('http://127.0.0.1:8000/all_employee')
        .then((response) => {
            data.employees = JSON.parse(response.data);
        })
        .catch((error) => {
            console.error(error);
        });
});

watch(searchText, async () => {
    await axios.get('http://127.0.0.1:8000/search_employee', { params: { s: searchText.value } })
        .then((response) => {
            data.employees = JSON.parse(response.data);
        })
        .catch((error) => {
            console.error(error);
        });
})

const onSearch = () => {
    
}


const confirmDelete = (id) => {
    if (confirm("Bạn có chắc muốn xóa không?"))
    {
        axios.delete('http://127.0.0.1:8000/delete_employee/' + id)
            .then((response) => {
                data.employees = response.data;
            })
            .catch((error) => {
                console.error(error);
            });
        window.location.reload();
    }
}

const addEmployee = () => {
    router.push(`/them-nhan-vien`);
}

const editEmployee = (id) => {
    router.push(`/chinh-sua-nhan-vien/` + id);
}
</script>

<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css">

    <div class="container">
        <div class="row, center-obj">
            <h1 style="margin-top: 10px;">Danh sách nhân viên chi nhánh Quảng Ninh</h1>
        </div>

        <div style="margin-bottom: 20px; margin-top: 10px;">
            <a-input-search v-model:value="searchText" placeholder="Search..." enter-button @search="onSearch" />
        </div>

        <table class="table table-striped table-bordered">
            <thead class="table-dark">
                <tr style="text-align: center;">
                    <th>Mã nhân viên</th>
                    <th>Họ và tên</th>
                    <th>Giới tính</th>
                    <th>Số điện thoại</th>
                    <th>Năm sinh</th>
                    <th>Chức vụ</th>
                    <th>Mã chi nhánh</th>
                    <th>Số giao dịch</th>
                    <th>Hành động</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="employee in data.employees" :key="employee.MaNV" class="body-content">
                    <td style="text-align: center;">{{ employee.MaNV }}</td>
                    <td style="text-align: center;">{{ employee.TenNV }}</td>
                    <td style="text-align: center;">{{ employee.GioiTinh }}</td>
                    <td style="text-align: center;">{{ employee.SDT }}</td>
                    <td style="text-align: center;">{{ employee.NamSinh }}</td>
                    <td style="text-align: center;">{{ employee.ChucVu }}</td>
                    <td style="text-align: center;">{{ employee.MaCN }}</td>
                    <td style="text-align: center;">{{ employee.SoGD }}</td>
                    <td class="buttons">
                        <a class="btn btn-primary" @click="editEmployee(employee.MaNV)" style="color: white;">Edit</a>
                        <a class="btn btn-danger" @click="confirmDelete(employee.MaNV)" style="color: white;">Delete</a>
                    </td>
                </tr>
            </tbody>
        </table>
        <a class="btn btn-success col-lg-12" style="color: white; font-size: 22px; margin-bottom: 10px;" @click="addEmployee">Thêm nhân viên mới</a>
    </div>
</template>

<style scoped>
.center-obj {
    display: flex;
    align-items: center;
    justify-content: center;
}

input[type="checkbox"] {
    transform: scale(1.3);
}

.buttons {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
}
</style>
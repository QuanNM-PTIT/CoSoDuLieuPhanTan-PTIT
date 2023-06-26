<script setup>
import axios from 'axios'
import { reactive, onMounted, ref, watch, createVNode } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const Errors = ref('');
const route = useRoute();
const employeeID = route.params.id;

const data = reactive(
    {
        employee: [],
    });

const backHome = () => {
    router.push(`/home`);
}

onMounted(() => {
    Errors.value = '';
    axios.get('http://127.0.0.1:8000/get_employee/' + employeeID)
        .then((response) => {
            data.employee = response.data;
        })
        .catch((error) => {
            console.log(error);
        });
})

const confirm = async () => {
    await axios.put('http://127.0.0.1:8000/update_employee/' + employeeID, {
        "MaNV": data.employee.MaNV,
        "TenNV": data.employee.TenNV,
        "GioiTinh": data.employee.GioiTinh,
        "SDT": data.employee.SDT,
        "NamSinh": data.employee.NamSinh,
        "ChucVu": data.employee.ChucVu,
        "MaCN": data.employee.MaCN
    })
        .then((response) => {
            if (response.data.includes("Cập nhật nhân viên thành công"))
                router.push(`/danh-sach-nhan-vien`);
            else {
                const str = response.data;
                const startStr = "[Microsoft][ODBC Driver 17 for SQL Server][SQL Server]";
                if (str.includes(startStr)) {
                    const startIndex = str.indexOf(startStr) + startStr.length;
                    Errors.value = str.substring(startIndex);
                    return;
                }
                Errors.value = response.data;
            }
        })
        .catch((error) => {
            Errors.value = 'Employee update failed.'
        });

};
</script>

<template>
    <main>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css">

        <div class="container">
            <div class="row" style="display: flex; justify-content: center; margin-top: 20px;">
                <h1>Thông tin chi tiết</h1>
            </div>

            <form class="form-content" @submit.prevent="confirm">
                <div class="col-12">
                    <label class="form-label">Mã nhân viên:</label>
                    <input type="text" class="form-control" id="inputAddress" name="name" v-model="data.employee.MaNV"
                        required>
                </div>

                <div class="col-12">
                    <label class="form-label">Tên nhân viên:</label>
                    <input type="text" class="form-control" id="inputAddress" name="name" v-model="data.employee.TenNV"
                        required>
                </div>

                <div class="col-12">
                    <label for="inputAddress" class="form-label">Giới tính:</label>
                    <input type="text" class="form-control" id="inputAddress" name="dob" v-model="data.employee.GioiTinh"
                        required>
                </div>

                <div class="col-12">
                    <label for="inputAddress" class="form-label">Số điện thoại:</label>
                    <input type="text" class="form-control" id="inputAddress" name="major" v-model="data.employee.SDT"
                        required>
                </div>

                <div class="col-12">
                    <label class="form-label">Năm sinh:</label>
                    <input type="text" class="form-control" id="inputAddress" name="name" v-model="data.employee.NamSinh"
                        required>
                </div>

                <div class="col-12">
                    <label for="inputAddress" class="form-label">Chức vụ:</label>
                    <input type="text" class="form-control" id="inputAddress" name="dob" v-model="data.employee.ChucVu"
                        required>
                </div>

                <div class="col-12">
                    <label for="inputAddress" class="form-label">Mã chi nhánh:</label>
                    <input type="text" class="form-control" id="inputAddress" name="major" v-model="data.employee.MaCN"
                        required>
                </div>

                <div class="col-lg-12">
                    <p class="text-danger">{{ Errors }}</p>
                </div>

                <div class="button-submit">
                    <a class="btn btn-primary" style="color: white;" @click="backHome">Trang chủ</a>
                    <button type="submit" class="btn btn-success" style="color: white;">Lưu</button>
                </div>
            </form>
        </div>
    </main>
</template>

<style scoped>
.col-lg-12 {
    margin-top: 20px;
    margin-bottom: 10px;
}

body {
    background-color: rgb(183, 233, 255);
}

.button-submit {
    display: flex;
    justify-content: center;
}

.button-submit a {
    margin-right: 5px;
}

input[type="checkbox"] {
    transform: scale(1.3);
}
</style>
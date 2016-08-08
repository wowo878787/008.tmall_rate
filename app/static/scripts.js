/**
 * Created by Nalake on 2016/8/7.
 */
$(document).ready(function () {
    //全局变量,记录上一步点击的索引和当前点击的索引
    //记录是否点击了不同的图片,记录当前点击图片的对应id
    var past_index, now_index, change, now_id;

    //遍历每一个缩略图 a标签
    $('.thumbnail').each(function (index) {
        //当点击这个a标签缩略图时
        $(this).mousedown(function () {
            //鼠标点下时更新现在的索引
            now_index = index;

            //当前点击的评论id引用位置
            now_id = $(this).attr('data-target');
            //当前点击的图片地址
            var now_pic = $(this).children().attr('src');
            //找到id引用位置修改图片链接
            $(now_id).children().attr('src', now_pic);

            //判断是否点击了不同的索引
            change = !(past_index == now_index);
        });

        $(this).mouseup(function (event) {
            //当前的image-viewer是否显示着
            var display = !($(now_id).css('display') == 'none');

            //鼠标抬起时更新上一步点击的索引
            past_index = now_index;

            //参考笔记真值表
            if (!change & display) {
                $(now_id).hide();
            }
            else {
                $(now_id).show();
            }

            //重新取一次image-viewer是否显示的值,如果显示着,就给他加个样式
            if (!($(now_id).css('display') == 'none')) {
                $(now_id).children().addClass('image_viewer_appear');
            }
        })
    });
});
title: Taxes in 2013
slug: taxes-en
timestamp: 12 Oct 2012 00:52
categories: ecume english
author: Luis Pedro Coelho <luis@luispedro.org>
---

Here's a little helper utility to let you know how much of your pay check will
be paid in taxes in Portugal:


.. raw:: html

    <form>
    <input id='salary' type="text" size="20" value="700" /><br />
    <input type='radio' name='perwhat' checked='yes' id='per12'>Per month (12 salaries)<br />
    <input type='radio' name='perwhat' id='per14'>Per month (14 salaries)<br />
    <input type='radio' name='perwhat' id='per1'>Per annum
    <p>
    <input type="button" value="Compute" id='subme' />
    </form>
    <div id='results'>

        <p>Your employer will spend <strong id='raw2'></strong> and you will
        receive <strong id='after_irs'></strong>.<br /> Your total tax
        contribution will <strong id='contribution'></strong> or, as a
        percentage, your rate will <strong
        id='contribution_rate'></strong>%.</p>

        <p><em>Details</em>: Before the "employer contribution", your salary
        will actually be €<strong id='raw'></strong> (of which you receive
        €<strong id='val'></strong>). Then you will pay an extra 11% to Social
        Security.  You will now have €<strong id='after_ss'></strong>, of
        which, assuming no rebates, you will pay <strong
        id='irs_rate'></strong>% as income tax (IRS).</p>

        <p>Of course, do not forget that most of what you spend this money on
        will be further taxed at 23%!</p>

    </div>
    <p id='error'>Something went wrong! Did you input in a number?</p>
    <script>
    $('#results').hide();
    $('#error').hide();

    function irs_paid(val) {
        var paid = 0;
        function sub0(y, x) {
            if (val <= y) return 0;
            if (val < x) return val - y;
            return x - y;
        }
        return sub0(0,7000)*0.145 + sub0(7000,20000)*0.285 + sub0(20000,40000)*0.37 + sub0(40000,80000)*0.45 + (val > 80000 ? val - 80000 : 0) * 0.48;
    }
    $('#subme').click(function() {
        try {
            $('#error').hide();
            var val = $('#salary').val();
            var checked = $('input[name=perwhat]:checked').attr('id');
            if (checked == 'per12') val *= 12.0;
            if (checked == 'per14') val *= 14.0;
            val = 1.0 * val;
            $('#val').text(val);
            var raw = val * 1.2375;
            $('#raw').text(Math.round(raw));
            $('#raw2').text(Math.round(raw));
            after_ss = 0.89 * val;
            
            $('#after_ss').text(Math.round(after_ss));

            irs = irs_paid(after_ss);
            irs_rate = irs / after_ss;
            $('#irs_rate').text(Math.round(irs_rate*100));
            $('#irs').text(Math.round(irs));
            after_irs = after_ss - irs;
            $('#after_irs').text(Math.round(after_irs));
            contribution = raw - after_irs;
            $('#contribution').text(Math.round(contribution));
            contribution_rate = contribution/raw;
            $('#contribution_rate').text(Math.round(contribution_rate*100));
            $('#results').show();
        } catch (err) {
            $('#error').show();
        }
        
        return false;
    });
    </script>

I got the rates from `Visão <http://visao.sapo.pt/conheca-os-novos-escaloes-do-irs=f690974>`__ and the social security website.


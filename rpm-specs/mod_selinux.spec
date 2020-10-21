%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

%define selinux_policy_types targeted mls minimum

Name: mod_selinux
Version: 2.4.4
Release: 16%{?dist}
Summary: Apache/SELinux plus module
License: ASL 2.0
URL: http://code.google.com/p/sepgsql/
Source0: http://sepgsql.googlecode.com/files/%{name}-%{version}.tgz
Source1: %{name}.conf
BuildRequires:  gcc
BuildRequires: httpd-devel >= 2.2.0 libselinux-devel checkpolicy >= 2.0.19 policycoreutils selinux-policy-devel
Requires: kernel >= 2.6.28 httpd >= 2.2.0 policycoreutils selinux-policy
Requires: httpd-mmn = %{_httpd_mmn}

%description
The Apache/SELinux plus is an extra module (mod_selinux.so) which enables
to launch contents-handler (it means both of references to static contents
and invocations of web applications) with individual and restrictive
privileges set, based on http authentication.
The mod_selinux.so generates a one-time worker thread for each request,
and it assigns the worker restrictive domain based on the authentication
prior to launching contents handlers.
It means we can apply valid access controls on web-applications, and
makes assurance operating system can prevent violated accesses, even if
web application contains security bugs or vulnerabilities.

%prep
%setup -q

%build
# mod_selinux.so
%{__make} %{?_smp_mflags} APXS=%{_httpd_apxs}

# mod_selinux.pp
for policy in %{selinux_policy_types}
do
    %{__make} NAME=${policy} -f %{?policy_devel_root}%{_datadir}/selinux/devel/Makefile
    mv %{name}.pp %{name}.${policy}.pp
done

%install
rm -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir}/httpd/modules
%{__install} -d %{buildroot}%{_datadir}/selinux

%{__make} install DESTDIR=%{buildroot}

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# httpd 2.4.x config
sed -n /^LoadModule/p %{SOURCE1} > 10-mod_selinux.conf
sed    /^LoadModule/d %{SOURCE1} > mod_selinux.conf
touch -r %{SOURCE1} *.conf
install -Dp 10-mod_selinux.conf %{buildroot}%{_httpd_modconfdir}/10-mod_selinux.conf
install -Dp mod_selinux.conf %{buildroot}%{_httpd_confdir}/mod_selinux.conf
%else
# httpd 2.2.x
install -Dp -m 644 %{SOURCE1}       %{buildroot}%{_httpd_confdir}/mod_selinux.conf
%endif

%{__install} -d %{buildroot}%{_datadir}/selinux/packages
for policy in %{selinux_policy_types}
do
    %{__install} -p -m 644 %{name}.${policy}.pp %{buildroot}%{_datadir}/selinux/packages
done

%post
/sbin/fixfiles -R %{name} restore || :

for policy in %{selinux_policy_types}
do
    %{_sbindir}/semodule -s ${policy} \
        -i %{_datadir}/selinux/packages/%{name}.${policy}.pp 2>/dev/null || :
done

%postun
# unload policy, if rpm -e
if [ $1 -eq 0 ]; then
    for policy in %{selinux_policy_types}
    do
        %{_sbindir}/semodule -s ${policy} -r %{name} 2>/dev/null || :
    done
fi

%files
%doc LICENSE README
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/*.conf
%endif
%config(noreplace) %{_httpd_confdir}/*.conf
%{_libdir}/httpd/modules/%{name}.so
%{_datadir}/selinux/packages/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 2.4.4-3
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun  6 2013 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.4.4-1
- fix security policy module

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.4.3
- fix build towards httpd-2.4.x

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2454-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May  1 2012 Joe Orton <jorton@redhat.com> - 2.2.2454-5
- packaging fixes (#803075)

* Tue May  1 2012 Joe Orton <jorton@redhat.com> - 2.2.2454-5
- packaging fixes (#803075)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2454-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2454-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec  4 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.2454-2
- rebuild for the base policy of F-13

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.2015-1
- update: add support to use translated format in MLS-range

* Wed May 27 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1938-1
- bugfix: it may returns OK, instead of HTTP_INTERNAL_SERVER_ERROR,
    when the contents handler crashed.

* Fri May 22 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1930-1
- rework: libselinux was dropped from explicit dependencies due to
    http://fedoraproject.org/wiki/Packaging/Guidelines#Explicit_Requires

* Tue May 19 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1904-1
- bugfix: update Makefile to allow to build for 64bit architecture

* Mon May 18 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1903-1
- rework: add selinux_merge_conf()
- rework: remove mod_authn_sepgsql, instead of documentation
          to use mod_authn_dbd with pgsql driver.

* Fri May 15 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1898-1
- rework: mod_authn_sepgsql cleanups
- update: README updates.

* Wed May 13 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1884-1
- rework: add mod_authn_sepgsql module
- rework: directives were reorganized
- rework: simultaneous usage with keep-alive

* Fri Apr 17 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1817-1
- bugfix: add kernel >= 2.6.28 because of typebounds feature

* Thu Apr 16 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1803-1
- rework: reverted to multi-threading design
- bugfix: security policy didn't allow prosess:{setcurrent}

* Wed Apr 15 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1800-1
- rework: worker was redesigned to use a process, instead of thread,
          on process_connection hook.
- rework: "selinuxAllowCaches" and "selinuxAllowKeepAlive" were added.
- rework: README was revised

* Tue Apr 14 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1795-1
- bugfix: install script didn't work correctly.
- update: add some of inline source comments.
- update: specfile improvement.

* Sun Apr 12 2009 KaiGai Kohei <kaigai@ak.jp.nec.com> - 2.2.1792-1
- Initial build

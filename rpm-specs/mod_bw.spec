%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}

Name:           mod_bw
Version:        0.8
Release:        26%{?dist}
Summary:        Bandwidth Limiter For Apache

License:        ASL 2.0
URL:            http://www.ivn.cl/apache
Source0:        http://www.ivn.cl/apache/files/source/mod_bw-%{version}.tgz
Source1:        mod_bw.conf
Patch0:         mod_bw-httpd24.patch

BuildRequires:  gcc
BuildRequires:  httpd-devel
Requires:       httpd-mmn = %{_httpd_mmn}

%description
mod_bw is a bandwidth administration module for Apache httpd 2.x

* Restricts the number of simultaneous connections per vhost/dir
* Limits the bandwidth for files on vhost/dir

%prep
%setup -q -n mod_bw
%patch0 -p1 -b .httpd24
mv mod_bw.txt mod_bw.txt.iso8859
iconv -f ISO-8859-1 -t UTF-8 mod_bw.txt.iso8859 > mod_bw.txt 


%build
%{_httpd_apxs} -Wc,"%{optflags}" -c mod_bw.c


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 .libs/mod_bw.so \
                 $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_bw.so
install -Dpm 644 %{SOURCE1} \
                 $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/mod_bw.conf



%files
%doc ChangeLog LICENSE TODO mod_bw.txt
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_bw.conf
%{_libdir}/httpd/modules/mod_bw.so


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 0.8-13
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Jan Kaluza <jkaluza@redhat.com> - 0.8-10
- Use proper httpd-2.4 patch

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 10 2012  - Jakub Hrozek <jhrozek@redhat.com> 0.8-8
- Fix compilation with httpd-2.4 (Jan Kaluza <jkaluza@redhat.com>)
- Provide backwards-compatible _httpd_apxs macro

* Wed Mar 14 2012 Jakub Hrozek <jhrozek@redhat.com> - 0.8-7
- Do not require httpd itself

* Wed Mar 14 2012 Jakub Hrozek <jhrozek@redhat.com> - 0.8-6
- Require httpd-mmn (#803067)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Jakub Hrozek <jhrozek@redhat.com> - 0.8-1
- initial packaging

Summary:	'top' for PostgreSQL process
Name:		pg_top
Version:	3.7.0
Release:	15%{?dist}
License:	BSD
Source0:	http://pgfoundry.org/frs/download.php/3504/%{name}-%{version}.tar.bz2
URL:		http://pgfoundry.org/projects/ptop
BuildRequires:	elfutils-libelf-devel
BuildRequires:	gcc
BuildRequires:	libpq-devel
BuildRequires:	readline-devel
Requires:	postgresql-server

%if 0%{?fedora} >= 10
BuildRequires:	systemtap-sdt-devel
%endif


%description
pg_top is 'top' for PostgreSQL processes. See running queries, 
query plans, issued locks, and table and index statistics.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%doc FAQ HISTORY LICENSE README TODO Y2K

%changelog
* Thu Feb 13 2020 Filipe Rosset <rosset.filipe@gmail.com> - 3.7.0-15
- Fix FTBFS rhbz#1799861

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.7.0-10
- add gcc into buildrequires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Filipe Rosset <rosset.filipe@gmail.com> - 3.7.0-1
- Rebuilt for new upstream version, spec cleanup
- Removed patches (already commited in upstream), fixes rhbz #991776 and #926327

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 26 2009 Alexey Torkhov <atorkhov@gmail.com> - 3.6.2-8
- Fix display of cumulative statistics (BZ#525763)

* Fri Sep 25 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.6.2-7
- starting building for EPEL too

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.6.2-5
- fix buildrequires, systemtap-sdt-devel is required for <sys/sdt.h>

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 - Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.6.2-3
- include %%{optflags} during compilation.
- include DOC files, including license file
- fix %%defattr
- remove pointless patch
- include BR elfutils-libelf-devel

* Wed Jan 21 2009 - Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.6.2-2
- Rebuild for Fedora 10

* Thu May 15 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.2-1
- Update to 3.6.2

* Sat Apr 12 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.2-0.1.beta3
- Rename to pg_top
- Update to 3.6.2 beta3

* Mon Mar 10 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.1-1
- Update to 3.6.1

* Sun Jan 20 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.1-1.beta3
- Update to 3.6.1-beta3

* Thu Dec 13 2007 - Devrim GUNDUZ <devrim@commandprompt.com> 3.6.1-1.beta2
- Initial RPM packaging for Fedora

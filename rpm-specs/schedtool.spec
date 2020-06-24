Name: schedtool       
Version:  1.3.0   
Release:  21%{?dist}
Summary:  Tool to query or alter process scheduling policy      

License:  GPLv2      
URL: http://freequaos.host.sk/schedtool/           
Source0: http://freequaos.host.sk/schedtool/%{name}-%{version}.tar.bz2   
      

BuildRequires:  gcc
%description
Schedtool interfaces with the Linux CPU scheduler. It allows the user to set 
and query the CPU-affinity and nice-levels of processes, as well as all 
scheduling policies, like batch or real-time (RR/FIFO) classes and 
their priorities

%prep
%setup -q

%build
make CFLAGS="%{optflags}" %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT
make install RELEASE="%{name}" DESTPREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT
chmod -x $RPM_BUILD_ROOT%{_mandir}/man8/schedtool.8.gz
cp -p CHANGES TODO TUNING $RPM_BUILD_ROOT%{_docdir}/%{name}/
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/INSTALL


%files
%{_bindir}/schedtool
%{_mandir}/man8/schedtool.8.gz
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/CHANGES
%doc %{_docdir}/%{name}/TUNING
%doc %{_docdir}/%{name}/TODO
%doc %{_docdir}/%{name}/SCHED_DESIGN

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 18 2013 Adel Gadllah <adel.gadllah@gmail.com> - 1.3.0-9
- Use unversioned doc dir RH #993873

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 11 2008 Adel Gadllah <adel.gadllah@gmail.com> 1.3.0-1
- Update to 1.3.0

* Fri Feb 08 2008 Adel Gadllah <adel.gadllah@gmail.com> 1.2.10-9
- Rebuild for gcc-4.3

* Tue Aug 21 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.10-8
- Rebuild for BuildID and ppc32 bug

* Fri Aug 03 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.10-7
- Update License tag

* Thu Jul 26 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.10-6
- Don't install SCHED_DESIGN (outdated Fedora uses CFS)

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 1.2.10-5
- rebuild for toolchain bug

* Thu Jul 24 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.10-4
- New upstream tarball

* Sun Jul 21 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.10-3
- Specfile cleanups (#248857)
- Install TODO

* Sun Jul 21 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.10-2
- Install CHANGES

* Sat Jul 20 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.10-1
- New upstream version
- Dropped patch (merged upstream)
- Don't install INSTALL

* Thu Jul 19 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.9-5
- Fix debuginfo
- Fix manpage permission

* Thu Jul 19 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.9-4
- Fix RPM_OPT_FLAGS not used again
- Fix docs permissions
- Preserve timestamps

* Thu Jul 19 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.9-3
- Remove duplicate docs

* Thu Jul 19 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.9-2
- Use RPM_OPT_FLAGS
- Use URL for Source

* Thu Jul 19 2007 Adel Gadllah <adel.gadllah@gmail.com> 1.2.9-1
- Initial Build

Name:           lockfile-progs
Version:        0.1.17
Release:        11%{?dist}
Summary:        Command-line programs to safely lock and unlock files and mailboxes

License:        GPLv2
# debian package, no real upstream source
URL:            http://packages.qa.debian.org/l/lockfile-progs.html
Source0:        http://ftp.de.debian.org/debian/pool/main/l/%{name}/%{name}_%{version}.tar.gz
BuildRequires:  liblockfile-devel
BuildRequires:  gcc


%description
lockfile-progs provide a method to lock and unlock mailboxes and  files
safely (via liblockfile).

%prep
%autosetup
sed -i 's/\(cd bin && ln \)/\1 -sf /' Makefile

%build
make %{_smp_mflags} CFLAGS='%{optflags}'

%check
make check

%install
mkdir -p %{buildroot}%{_bindir}
cp -r --preserve=all bin/* %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -r --preserve=all man/* %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/lockfile-check
%{_bindir}/lockfile-create
%{_bindir}/lockfile-remove
%{_bindir}/lockfile-touch
%{_bindir}/mail-lock
%{_bindir}/mail-touchlock
%{_bindir}/mail-unlock
%{_mandir}/man1/*.1*
%doc COPYING

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Matthias Runge <mrunge@redhat.com> - 0.1.17-6
- add gcc build requirement

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Matthias Runge <mrunge@redhat.com> - 0.1.17-1
- update to 0.1.17 (rhbz#1367543)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 14 2010 Matthias Runge <mrunge@matthias-runge.de> 0.1.15-2
- correct make-invocation, move it to build
- COPYING in as doc
- remove {__-invocations, replace by plain calls

* Fri Aug 13 2010 Matthias Runge <mrunge@matthias-runge.de> 0.1.15-1
- new version from upstream

* Fri Aug 13 2010 Matthias Runge <mrunge@matthias-runge.de> 0.1.13-2
- cleanup

* Wed Apr 28 2010 Matthias Runge <mrunge@matthias-runge.de> 1.3.8-1
- initial spec

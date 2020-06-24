%global commit0 cd2610e0fa1c6a90e8e4e4cfe06db1b474e752bb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global snapdate 20200517

%global __python %{__python3}

Name:           icestorm
Version:        0
Release:        0.12.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        Lattice iCE40 FPGA bitstream creation/analysis/programming tools
License:        ISC
URL:            http://www.clifford.at/%{name}/
Source0:        https://github.com/cliffordwolf/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

# Fedora-specific patch for datadir
Patch1:         %{name}-datadir.patch

BuildRequires:  gcc-c++
BuildRequires:  python%{python3_pkgversion} libftdi-devel

%description
Project IceStorm aims at documenting the bitstream format of Lattice iCE40
FPGAs and providing simple tools for analyzing and creating bitstream files.

%prep
%setup -q -n %{name}-%{commit0}
%patch1 -p1 -b .datadir

# fix shebang lines in Python scripts
find . -name \*.py -exec sed -i 's|/usr/bin/env python3|/usr/bin/python3|' {} \;
# get rid of .gitignore files in examples
find . -name \.gitignore -delete

%build
%global moreflags -I/usr/include/libftdi1
make %{?_smp_mflags} \
     CFLAGS="%{optflags} %{moreflags}" \
     CXXFLAGS="%{optflags} %{moreflags}" \
     PREFIX="%{_prefix}" \
     CHIPDB_SUBDIR="%{name}" \
     LDFLAGS="$RPM_LD_FLAGS"

%install
%make_install PREFIX="%{_prefix}"
chmod +x %{buildroot}%{_bindir}/icebox.py
mv %{buildroot}%{_datarootdir}/icebox %{buildroot}%{_datarootdir}/%{name}
mv %{buildroot}%{_bindir}/iceboxdb.py %{buildroot}%{_datarootdir}/%{name}
install -pm644 icefuzz/timings_*.txt %{buildroot}%{_datarootdir}/%{name}

# We could do a minimal check section by running make in the example
# directories, but that depends on arachne-pnr, which depends on this
# package, so it would create a circular dependency.

%files
%license README
%doc examples
%{_bindir}/*
%{_datarootdir}/%{name}

%changelog
* Sun May 17 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.12.20200517gitcd2610e
- Update to newer snapshot
- Spec file: remove gcc10 patch (now in upstream)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20190823git9594931
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0-0.10.20190823git9594931
- Fix missing #include for gcc-10

* Fri Aug 23 2019 Gabriel Somlo <gsomlo@gmail.com> - 0-0.9.20190823git9594931
- Update to newer snapshot
- Spec file: fix source URL; add 'snapdate' variable

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20190311gitfa1c932
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Lubomir Rintel <lkundrak@v3.sk> - 0-0.7.20190311gitfa1c932
- Update to a newer snapshot
- Package the timing files

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20170914git5c4d4db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170914git5c4d4db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Lubomir Rintel <lkundrak@v3.sk> 0-0.5.20170914git5c4d4db
- Fix the chipdb path for icetime

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170914git5c4d4db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Eric Smith <brouhaha@fedoraproject.org> 0-0.3.20170914git5c4d4db
- Updated per review comments.
- Updated to latest upstream.

* Sat Dec 10 2016 Eric Smith <brouhaha@fedoraproject.org> 0-0.2.20161101git01b9822
- Updated per review comments.
- Updated to latest upstream.

* Mon Sep 12 2016 Eric Smith <brouhaha@fedoraproject.org> 0-0.1.20160904git0b4b038
- Initial version.

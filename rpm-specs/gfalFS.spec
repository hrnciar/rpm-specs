
Name:			gfalFS
Version:		1.5.2
Release:		7%{?dist}
Summary:		Filesystem client based on GFAL 2.0
License:		ASL 2.0
URL:			https://svnweb.cern.ch/trac/lcgutil/wiki/gfal2
# git clone https://gitlab.cern.ch/dmc/gfalFS.git gfalFS-1.5.2
# pushd gfalFS-1.5.2
# git checkout v1.5.2
# git submodule init
# popd
# tar czf gfalFS-1.5.2.tar.gz gfalFS-1.5.2 --exclude-vcs
Source0:		%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:		cmake
BuildRequires:		gfal2-devel
BuildRequires:		fuse-devel

Requires:		fuse%{?_isa}
Provides:		gfal2-fuse = %{version}

%description
gfalFS is a filesystem based on FUSE capable of operating on remote storage
systems managed by GFAL 2.0. This include the common file access protocols 
in lcg ( SRM, GRIDFTP, DCAP, RFIO, LFN, ...). The practical effect is that
the user can seamlessly interact with grid and cloud storage systems just 
as if they were local files.

%clean
rm -rf %{buildroot};
make clean

%prep
%setup -q

%build
%cmake \
-DDOC_INSTALL_DIR=%{_docdir}/%{name}-%{version} .
make %{?_smp_mflags}

%install
rm -rf %{buildroot}; 
make DESTDIR=%{buildroot} install

%files
%{_bindir}/gfalFS
%{_bindir}/gfalFS_umount
%{_mandir}/man1/*
%{_docdir}/%{name}-%{version}/DESCRIPTION
%{_docdir}/%{name}-%{version}/VERSION
%{_docdir}/%{name}-%{version}/LICENSE
%{_docdir}/%{name}-%{version}/README
%{_docdir}/%{name}-%{version}/RELEASE-NOTES
%{_docdir}/%{name}-%{version}/readme.html

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Alejandro Alvarez <aalvarez at cern.ch> - 1.5.2-1
- Update 1.5.2 of gfalFS

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Alejandro Alvarez <aalvarez at cern.ch> - 1.5.0-1
 - Update 1.5.0 of gfalFS

* Mon Oct 28 2013 Adrien Devresse <adevress at cern.ch> - 1.4.0-3
 - Update 1.4.0 of gfalFS

* Wed Mar 20 2013 Adrien Devresse <adevress at cern.ch> - 1.2.0-0
 - fix a EIO problem with the gfal 2.0 http plugin 

* Thu Nov 29 2012 Adrien Devresse <adevress at cern.ch> - 1.0.1-0
 - fix a 32 bits off_t size problem with gfal 2.1


* Fri Jul 20 2012 Adrien Devresse <adevress at cern.ch> - 1.0.0-1
 - initial 1.0 release
 - include bug fix for srm and gsiftp url for fgettr

* Thu May 03 2012 Adrien Devresse <adevress at cern.ch> - 1.0.0-0.3.20120503010snap
 - bug correction with fgetattr on gsiftp / srm file system
 - minor changes applied from the fedora review comments

* Thu May 03 2012 Adrien Devresse <adevress at cern.ch> - 1.0.0-0.2.2012050202snap
 - improve global EPEL compliance.

* Mon Nov 14 2011 Adrien Devresse <adevress at cern.ch> - 1.0.0-0.2.2012041515snap
 - Initial gfalFS 1.0 preview release

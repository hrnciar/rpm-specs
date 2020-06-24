Name:           rnv
Version:        1.7.11
Release:        19%{?dist}
Summary:        Implementation of Relax NG Compact Syntax validator in ANSI C

License:        BSD
URL:            http://sourceforge.net/projects/rnv/
Source0:        http://downloads.sourceforge.net/project/rnv/Sources/%{version}/%{name}-%{version}.tar.xz
Source1:        arx.1
Source2:        xsdck.1
Source3:        rvp.1
Source4:        metainfo.xml
# Sent upstream via email
Patch0:    %{name}.system-paths-lookup.patch
# Adds docbook to arx.conf, because upstream version doesn't ship any useful schemas
Patch1:    %{name}.arx-conf-with-docbook.patch
Patch2:    %{name}.rvp-pl-wrong-interpreter.patch

BuildRequires:  expat-devel
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake

Requires:       docbook5-schemas

%package -n vim-rnv
Summary:        Vim plugin for validating XML files against Relax NG Compact schemas using RNV

Requires:       vim-common
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description
RNV uses Relax NG compact syntax schemas to check if a given XML file is
valid in respect to the language defined by the Relax NG schema. RNV
uses Expat for XML parsing.

%description -n vim-rnv
Vim plugin providing redefined make command that validates
XML files against Relax NG schemas.

%prep
%setup -q
%patch0
%patch1
%patch2

cp -p %SOURCE1 .
cp -p %SOURCE2 .
cp -p %SOURCE3 .

%build
autoreconf -i
%configure --enable-dxl
make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/appdata
install -m644 %SOURCE4 %{buildroot}%{_datadir}/appdata/vim-rnv.metainfo.xml

%files
%{_bindir}/rnv
%{_bindir}/arx
%{_bindir}/xsdck
%{_bindir}/rvp
%{_mandir}/man1/rnv.1*
%{_mandir}/man1/rvp.1*
%{_mandir}/man1/arx.1*
%{_mandir}/man1/xsdck.1*
%dir %{_sysconfdir}/rnv
%config(noreplace) %{_sysconfdir}/rnv/arx.conf
%doc COPYING ChangeLog readme.txt
%docdir %{_docdir}/rnv/examples
%doc %{_docdir}/rnv/examples/rvp.py*
%doc %{_docdir}/rnv/examples/rvp.pl

%files -n vim-rnv
%{_datadir}/vim/vimfiles/plugin/rnv.vim
%{_datadir}/appdata/vim-rnv.metainfo.xml

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Simacek <msimacek@redhat.com> - 1.7.11-15
- Add BR on gcc and make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 28 2015 Michael Simacek <msimacek@redhat.com> - 1.7.11-9
- Add metainfo file for vim-rnv

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Michael Simacek <msimacek@redhat.com> - 1.7.11-5
- Modified subpackages to comply to Package Guidelines

* Fri Aug 16 2013 Michael Simacek <msimacek@redhat.com> - 1.7.11-4
- Package autoreconf'ed instead of patching Makefile.in

* Thu Aug 15 2013 Michael Simacek <msimacek@redhat.com> - 1.7.11-3
- Renamed vim plugin subpackage to follow naming guidelines

* Wed Aug 14 2013 Michael Simacek <msimacek@redhat.com> - 1.7.11-2
- Patched arx, rnv and build to use global config file /etc/arx.conf and global grammars in /usr/shar/rnv/grammars
- Created man pages for arx, rvp and xsdck

* Thu Aug 08 2013 Michael Simacek <msimacek@redhat.com> - 1.7.11-1
- Initial version

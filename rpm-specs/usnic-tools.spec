Name:           usnic-tools
Version:        1.1.2.1
Release:        5%{?dist}
Summary:        Diagnostic tool for Cisco usNIC devices
License:        GPLv2 or BSD
Url:            https://github.com/cisco/usnic_tools
Source0:        https://github.com/cisco/usnic_tools/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  libfabric-devel >= 1.3.0
BuildRequires:  gcc
ExcludeArch:    %{arm}

%description
This is a simple tool for extracting some diagnostics and informational
meta data out of Cisco usNIC devices using the Cisco usNIC extensions
in libfabric.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%{make_install}

%files
%{_bindir}/*
%license COPYING
%doc README.md
%{_mandir}/man1/usnic_devinfo.1.gz

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun  6 2018 Honggang Li <honli> - 1.1.2.1-1
- Rebase to latest upstream release 1.1.2.1
- Resolves: bz1441446, bz1556522

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 17 2016 Honggang Li <honli> - 1.1.1.0-1
- Rebase to latest upstream release v1.1.1.0.

* Thu Apr 14 2016 Honggang Li <honli@redhat.com> - 1.1.0.0-3
- Use a short summary tag.
- Take smaller size bz2 source tar ball.
- Add gcc as build requires.
- Enable verbose mode for compiling.
- Let the type "char" be signed to build it on ARM platform.

* Thu Apr 14 2016 Honggang Li <honli@redhat.com> - 1.1.0.0-2
- Improve summary tag.
- Use a more relevant URL.
- Remove license comment.
- Add README.md as doc.

* Thu Apr 14 2016 Honggang Li <honli@redhat.com> - 1.1.0.0-1
- Import usnic-tools for Fedora.

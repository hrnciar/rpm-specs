Name:           iucode-tool
Version:        2.3.1
Release:        2%{?dist}
Summary:        iucode_tool is a program to manipulate microcode update collections for Intel i686 and X86-64 system processors, and prepare them for use by the Linux kernel

License:        GPlv2+
URL:            https://gitlab.com/iucode-tool/iucode-tool
Source0:	https://gitlab.com/iucode-tool/iucode-tool/-/archive/v%{version}/iucode-tool-v%{version}.tar.gz

# This tool is only useful for x86_64 and i686
ExclusiveArch:	%{ix86} x86_64

BuildRequires:  gcc autoconf automake
%description
iucode_tool is a program to manipulate microcode update collections for Intel i686 and X86-64 system processors, and prepare them for use by the Linux kernel.

%prep
%autosetup -n iucode-tool-v%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README TODO NEWS
%doc %{_mandir}/man*/*
%{_sbindir}/iucode_tool


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 2.2-1
- Initial packaging

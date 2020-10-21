Name:           yank
Version:        0.8.3
Release:        10%{?dist}
Summary:        Tool for selecting and copying text from stdin without a mouse

License:        MIT
URL:            https://github.com/mptre/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

Requires:       bash

# Executable 'yank' already exists in another package (EMBOSS-6.6.0-3.fc24.x86_64). Binary is 'yank-cli'.
%global name_change yank-cli

%description
Read input from stdin and display a selection interface that allows a field 
to be selected and copied to the clipboard. Fields are either recognized by 
a regular expression using the -g option or by splitting the input on a 
delimiter sequence using the -d option.

%prep
%autosetup

%build
CFLAGS=${RPM_OPT_FLAGS} %make_build PROG=%{name_change}

%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir} INSTALL_PROGRAM='install -m 0755' PROG=%{name_change}

# Provide the same manpage for both 'yank' and 'yank-cli'
ln -s %{_mandir}/man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name_change}.1

%files
%{_bindir}/%{name_change}
%{_mandir}/man1/%{name}*
%{_mandir}/man1/%{name_change}*
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 nmilosev <nmilosev@fedoraproject.org> - 0.8.3-5
- New upstream version (same version code)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 nmilosev <nmilosev@fedoraproject.org> - 0.8.3-1
- Upstream: 0.8.3
* Sun Feb 19 2017 nmilosev <nmilosev@fedoraproject.org> - 0.8.2-1
- Upstream: 0.8.2
* Sat Feb 18 2017 nmilosev <nmilosev@fedoraproject.org> - 0.8.1-1
- Integrated patches for debuginfo and name changing to the upstream
* Thu Feb 16 2017 nmilosev <nmilosev@fedoraproject.org> - 0.8.0-1
- Initial RPM for Fedora

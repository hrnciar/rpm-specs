#
# spec file for package smbcmp
#

Name:		smbcmp
Version:	0.1
Release:	6%{?dist}
License:	GPLv3+
Summary:	Small curses utility to diff, compare and debug SMB network traces
URL:		https://github.com/smbcmp/smbcmp
Group:		Development/Tools/Debuggers
Source0:	https://github.com/smbcmp/smbcmp/archive/v0.1/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3 >= 3.4
BuildRequires:	python3-setuptools
Requires:	wireshark-cli

%description
Small curses utility to diff, compare and debug SMB network traces.

%package gui
Summary:	GUI version of smbcmp
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python3-wxpython4

%description gui
smbcmp is a debug tool to diff and compare network captures aimed
towards SMB traffic. This is the GUI version of smbcmp based on the
wxWidget toolkit.

%prep
%autosetup -p1

%build
# Workaround as there is no -lboost_python3
sed -i 's|curses||' setup.py
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/smbcmp/
%{python3_sitelib}/smbcmp*egg-info*

%files gui
%{_bindir}/%{name}-gui

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Guenther Deschner <gdeschner@redhat.com> - 0.1-3
- Add missing dist tag

* Wed Oct 02 2019 Guenther Deschner <gdeschner@redhat.com> - 0.1-2
- Initial package

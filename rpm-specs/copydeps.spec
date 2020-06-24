Name:    copydeps
Version: 4.0
Release: 4%{?dist}
Summary: Find and copy .so / .dll files required by a binary executable
License: GPLv3+

URL: https://github.com/suve/copydeps

%global gittag release-v.%{version}
Source0: %{URL}/archive/%{gittag}/%{name}-%{gittag}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel >= 3.5

%{?python_enable_dependency_generator}

Requires: binutils, coreutils
Requires: python3 >= 3.5


%description
%{name} is a small program that can be used to find and copy all .so / .dll
files needed by a program to run. This can be useful when you want to bundle
an application together with all its dependencies.


%prep
%setup -q -n %{name}-%{gittag}


%build
%py3_build


%install
%py3_install

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 -p %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1


%files
%doc README.txt
%license LICENCE.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0-4
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 08 2019 Artur Iwicki <fedora@svgames.pl> - 4.0-1
- Initial packaging

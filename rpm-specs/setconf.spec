Name:           setconf
Version:        0.7.7 
Release:        3%{?dist}
Summary:        Utility for changing settings in configuration text files 

License:        GPLv2
URL:            http://setconf.roboticoverlords.org/ 
Source0:        https://github.com/xyproto/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Patch#:       setconf-version-description.patch
Patch0:         setconf-0.7.6-rm_sb.patch
Patch2:         setconf-0.7.7-add_man.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildArch:      noarch

%description
Setconf is small utility that can be used for
changing settings in configuration text files. 

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%check
%{__python3} setconf.py --test
awk '/^..\/setconf.py/ { print "%{__python3} " $0; next } { print }' testcases/test.sh >testcases/py3_test.sh
chmod a+x testcases/py3_test.sh
cd testcases/ && ./py3_test.sh

%install
%py3_install

%files
%license COPYING
%doc README.md
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/__pycache__/%{name}.*.pyc
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Jan Macku <jamacku@redhat.com> - 0.7.7-2
- Fix names of patches in spec
- Fix Patch1 to match the source

* Tue Jul 07 2020 Jan Macku <jamacku@redhat.com> - 0.7.7-1
- New release - setconf 0.7.7

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Jan Macku <jamacku@redhat.com> - 0.7.6-1 
- Init setconf package  

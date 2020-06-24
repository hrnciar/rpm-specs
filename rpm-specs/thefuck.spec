Name: thefuck
Version: 3.15
Release: 11%{?dist}
Summary: App that corrects your previous console command
License: MIT
URL: https://github.com/nvbn/thefuck
Source0: https://github.com/nvbn/%{name}/archive/%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-colorama
BuildRequires: python3-psutil
BuildRequires: python3-pip
BuildRequires: python3-six
BuildRequires: python3-decorator
BuildRequires: python3-pytest
BuildRequires: python3-mock
Requires: python3
Requires: python3-psutil
Requires: python3-six
Requires: python3-colorama
BuildArch: noarch

%description
This application corrects your previous console command.
If you use BASH, you should add these lines to your .bashrc:
alias fuck='eval $(thefuck $(fc -ln -1)); history -r'
alias FUCK='fuck'
For other shells please check /usr/share/doc/thefuck/README.md

%prep
%setup -q
sed -i -e '/^#!\//, 1d' *.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT

%files
%{_bindir}/thefuck
%{_bindir}/fuck
%{python3_sitelib}/thefuck-%{version}-*egg-info
%{python3_sitelib}/thefuck
%doc README.md 
%license LICENSE.md

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.15-11
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.15-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.15-8
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.15-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Matias Kreder <delete@fedoraproject.org> 3.15-1
- Updated to thefuck 3.15

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Matias Kreder <delete@fedoraproject.org> 3.2-3
- Added buildrequires

* Wed Nov 18 2015 Matias Kreder <delete@fedoraproject.org> 3.2-1
- Updated to thefuck 3.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul 2 2015 Matias Kreder <delete@fedoraproject.org> 1.46-1
- Initial spec

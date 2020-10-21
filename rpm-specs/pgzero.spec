Name:           pgzero
Version:        1.2
Release:        10%{?dist}
Summary:        A zero-boilerplate 2D games framework

License:        LGPLv3 and ASL 2.0 and CC-BY-SA and CC0 and MIT and OFL
# pgzero module and runner under LGPLv3
# examples/basic/fonts/Cherry_Cream_Soda and Roboto_Condensed under ASL 2.0
# examples/lander/lander.py under CC-BY-SA
# examples/basic/fonts/bubblegum_sans.ttf under CC0
# examples/memory/ under MIT
# examples/basic/fonts/Boogaloo and Bubblegum_Sans under OFL
URL:            http://pypi.python.org/pypi/pgzero
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pygame
BuildRequires:  python3-numpy

%{?python_provide:%python_provide python3-%{name}}
 
Requires:       python3-pygame
Requires:       python3-setuptools
Requires:       python3-numpy

%description
Pygame Zero A zero boilerplate games programming framework for Python 3, based
on Pygame. Pygame Zero consists of a runner pgzrun that will run a
Pygame Zero script with a full game loop and a range of useful builtins.

%prep
%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Some tests cannot be run in a headles environment without display
rm test/test_screen.py test/test_actor.py test/test_sound_formats.py
# test_tone.py is broken https://github.com/lordmauve/pgzero/issues/66
sed -i -e 's/from tone/from pgzero.tone/' test/test_tone.py
sed -i -e 's/valid note, /valid note. /' test/test_tone.py
%{__python3} -m unittest discover test/

%files
%license COPYING
%doc README.txt examples
%{_bindir}/pgzrun
%{python3_sitelib}/%{name}
%{python3_sitelib}/pgzrun.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-2
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Lumir Balhar <lbalhar@redhat.com> - 1.2-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Lumir Balhar <lbalhar@redhat.com> - 1.1-1
- Initial package.

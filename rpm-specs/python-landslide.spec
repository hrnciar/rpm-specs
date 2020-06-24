%global pkgname landslide
%global commit	9a70c0f4fd00c17cffbfd0da7ffb87da118ff9b0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		python-landslide
Version:	1.1.3
Release:	16%{?dist}
Summary:	Lightweight markup language-based html5 slideshow generator
License:	ASL 2.0
URL:		https://pypi.python.org/pypi/landslide
Source0:	https://github.com/adamzap/%{pkgname}/archive/%{commit}/%{pkgname}-%{version}-%{shortcommit}.tar.gz

BuildArch:	noarch


%description
Takes your Markdown, ReST, or Textile file(s) and generates 
fancy HTML5 slideshows.

%package -n python3-%{pkgname}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-sphinx

Requires:	python3-jinja2
Requires:	python3-markdown
Requires:	python3-pygments
Requires:	python3-docutils
Requires:	python3-textile

%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
Takes your Markdown, ReST, or Textile file(s) and generates 
fancy HTML5 slideshows.

%prep
%autosetup -n %{pkgname}-%{commit}
# Change shebang to recognized the default interpreter installed 
# from system-wide
sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' src/landslide/main.py
# Remove bundled egg-info
rm -rf src/landslide.egg-info

%build
%py3_build

PYTHONPATH=$(pwd) make -C docs html
rm -f docs/_build/html/.buildinfo

%install
%py3_install
find %{buildroot} -name 'main.py' | xargs chmod 0755
 
%files -n python3-%{pkgname}
%doc CHANGELOG.md README.md docs/_build/html
%license LICENSE
%{_bindir}/landslide
%{python3_sitelib}/landslide
%{python3_sitelib}/landslide-*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.3-6
- Fix shebang to avoid depending on both Python 2 and Python 3
- Package python3- subpackage

* Wed Feb 22 2017 Jan Beran <jberan@redhat.com> - 1.1.3-5
- Provides Python 3 package

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 1 2015 Eduardo Echeverria  <echevemaster@gmail.com> - 1.1.3-1
- Initial packaging

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 1.1.1-2
- Change shebang to recognize the installed default interpreter.
- Remove MANIFEST.in from documentation

* Sun Jul 07 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 1.1.1-1
- Initial packaging


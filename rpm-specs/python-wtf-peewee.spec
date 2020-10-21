%global srcname wtf-peewee

Name:		python-wtf-peewee
Version:	3.0.0
Release:	8%{?dist}
Summary:	WTForms integration for peewee models

License:	MIT
URL:		https://github.com/coleifer/wtf-peewee/
Source0:	https://pypi.python.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	pyproject-rpm-macros

%description
Wtf-peewee, based on the code found in wtforms.ext, provides a bridge between
peewee models and wtforms, mapping model fields to form fields.

%package -n python3-%{srcname}
Summary:        WTForms integration for peewee models

%description -n python3-%{srcname}
Wtf-peewee, based on the code found in wtforms.ext, provides a bridge between
peewee models and wtforms, mapping model fields to form fields.


%prep
%setup -q -n %{srcname}-%{version}

# Remove shebang and executable bits from runtests.py
chmod -x runtests.py
sed -i '1d' runtests.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wtfpeewee

%check
%{__python3} setup.py test


%files -n python3-%{srcname} -f %pyproject_files
%doc README.md
%license LICENSE

%changelog
* Tue Sep 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.0.0-8
- Convert the package to pyproject macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Charalampos Stratakis <cstratak@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.2.6-9
- Remove the python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.6-5
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-2
- Rebuild for Python 3.6

* Mon Nov 07 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Mon Jun 06 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.2.3-4
- Provide a python 3 subpackage
- Add license tag
- Modernize SPEC

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 09 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Matej Stuchlik <mstuchli@redhat.com> - 0.2.2-1
- Updated to 0.2.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 mstuchli <mstuchli@redhat.com> - 0.2.1-1
- Initial spec

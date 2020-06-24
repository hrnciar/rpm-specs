%global modname alembic

Name:             python-alembic
Version:          1.4.2
Release:          2%{?dist}
Summary:          Database migration tool for SQLAlchemy

License:          MIT
URL:              https://pypi.io/project/alembic
Source0:          %pypi_source alembic

BuildArch:        noarch

BuildRequires:    help2man

BuildRequires:    python3-devel
BuildRequires:    python3-sqlalchemy >= 1.1
BuildRequires:    python3-mako
BuildRequires:    python3-nose
BuildRequires:    python3-setuptools
BuildRequires:    python3-mock
BuildRequires:    python3-dateutil
BuildRequires:    python3-editor
BuildRequires:    python3-pytest


%global _description\
Alembic is a new database migrations tool, written by the author of\
SQLAlchemy.  A migrations tool offers the following functionality:\
\
* Can emit ALTER statements to a database in order to change the structure\
  of tables and other constructs.\
* Provides a system whereby "migration scripts" may be constructed; each script\
  indicates a particular series of steps that can "upgrade" a target database\
  to a new version, and optionally a series of steps that can "downgrade"\
  similarly, doing the same steps in reverse.\
* Allows the scripts to execute in some sequential manner.\
\
Documentation and status of Alembic is at http://readthedocs.org/docs/alembic/

%description %_description


%package -n python3-alembic
Summary:          %summary

Requires:         python3-sqlalchemy >= 1.1
Requires:         python3-mako
Requires:         python3-setuptools
Requires:         python3-editor
Requires:         python3-dateutil
%{?python_provide:%python_provide python3-alembic}


%description -n python3-alembic %_description

%prep
%autosetup -p1 -n %{modname}-%{version}


%build
%py3_build

%{__mkdir_p} bin
echo 'python3 -c "import alembic.config; alembic.config.main()" $*' > bin/alembic
chmod 0755 bin/alembic
help2man --version-string %{version} --no-info -s 1 bin/alembic > alembic.1


%install

install -d -m 0755 %{buildroot}%{_mandir}/man1

%py3_install
mv %{buildroot}/%{_bindir}/%{modname} %{buildroot}/%{_bindir}/%{modname}-3
ln -s %{modname}-3 %{buildroot}/%{_bindir}/%{modname}-%{python3_version}
install -m 0644 alembic.1 %{buildroot}%{_mandir}/man1/alembic-3.1
ln -s alembic-3.1 %{buildroot}%{_mandir}/man1/alembic-%{python3_version}.1

ln -s %{modname}-%{python_version} %{buildroot}/%{_bindir}/%{modname}
ln -s alembic-%{python_version}.1 %{buildroot}%{_mandir}/man1/alembic.1


%check
py.test-3


%files -n python3-%{modname}
%doc LICENSE README.rst CHANGES docs
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*
%{_bindir}/%{modname}
%{_mandir}/man1/alembic.1*
%{_bindir}/%{modname}-3
%{_bindir}/%{modname}-%{python3_version}
%{_mandir}/man1/alembic-3.1*
%{_mandir}/man1/alembic-%{python3_version}.1*


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.9

* Sun Mar 22 2020 Carl George <carl@george.computer> - 1.4.2-1
- Latest upstream rhbz#1808866

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1784129).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1 (#1767518).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.3.1

* Fri Sep 27 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1 (#1754016).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.2.1

* Tue Sep 17 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.0-2
- Drop python2-alembic (#1751088).

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.0-1
- Upgrade to 1.1.0 (#1747053).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.1.0

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.11-3
- Rebuilt for Python 3.8

* Mon Jul 22 2019 Petr Viktorin <pviktori@redhat.com> - 1.0.11-2
- Make /usr/bin/alembic point to alembic-3 on Fedora 31+
  See https://fedoraproject.org/wiki/Changes/Python_means_Python3
- Avoid absolute symlinks
- Conditionalize the Python 2/Python 3 parts with bcond

* Sun Jun 30 2019 Kevin Fenzi <kevin@scrye.com> - 1.0.11-1
- Update to 1.0.11. Fixes bug #1723981

* Wed Jun 19 2019 Troy Dawson <tdawson@redhat.com> - 1.0.10-1.1
- Make python2 optional
- Do not build python2 on RHEL8

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10 (#1700050).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.0.10

* Thu Mar 28 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8 (#1685262).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.0.8

* Tue Feb 05 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.0.7-1
- Update to 1.0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-6
- Rebuilt for Python 3.7

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-5
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.7-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.9.7-3
- The python3-alembic package now provides only alembic-3 and alembic-3.y.
- The python2-alembic package now provides alembic, alembic-2, and alembic-2.y.

* Sat Jan 27 2018 Ralph Bean <rbean@redhat.com> - 0.9.7-2
- The python3-alembic package now provides the alembic executable.

* Thu Jan 18 2018 Ralph Bean <rbean@redhat.com> - 0.9.7-1
- new version
- New dependency on python-dateutil.

# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
%if 0%{?fedora} < 30
%global with_py2 1
%else
%global with_py2 0
%endif
%global srcname     hdfs
%global sum         HdfsCLI: API and command line interface for HDFS

Name:       python-%{srcname}
Version:    2.5.8
Release:    5%{?dist}
Summary:    %{sum}

License:    MIT
URL:        https://github.com/mtth/%{srcname}
Source0:    https://github.com/mtth/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description Python (2 and 3) bindings for the WebHDFS (and HttpFS) \
API, supporting both secure and insecure clusters.  Command line interface to \
transfer files and start an interactive client shell, with aliases for \
convenient name-node URL caching.  Additional functionality through optional \
extensions: Avro, to read and write Avro files directly from HDFS.  data-frame, \
to load and save Pandas data-frames.  Kerberos, to support Kerberos \
authenticated clusters.

%description
%{_description}

%if %{with_py2}
%package -n python2-%{srcname}
Summary:        %{sum}
BuildRequires:  python2-devel
BuildRequires:  %{py2_dist setuptools}
BuildRequires:  %{py2_dist six}
BuildRequires:  %{py2_dist fastavro}
BuildRequires:  %{py2_dist pandas}
BuildRequires:  %{py2_dist requests-kerberos}
BuildRequires:  %{py2_dist nose}
BuildRequires:  %{py2_dist mock}
Requires:       %{py2_dist six}
Requires:       %{py2_dist requests}
Requires:       %{py2_dist docopt}
Requires:       %{py2_dist fastavro}
Requires:       %{py2_dist pandas}
Requires:       %{py2_dist requests-kerberos}
Requires:   %{py2_dist mock}

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{_description}
%endif

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist fastavro}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist requests-kerberos}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist mock}
Requires:       %{py3_dist six}
Requires:       %{py3_dist requests}
Requires:       %{py3_dist docopt}
Requires:       %{py3_dist fastavro}
Requires:       %{py3_dist pandas}
Requires:       %{py3_dist requests-kerberos}
Requires:   %{py3_dist mock}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%package doc
Summary:    Documentation for %{name}
BuildRequires:  %{py3_dist sphinx}
# Should docs require the main package?

%description doc
%{_description}

%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info

%build
%if %{with_py2}
%py2_build
%endif
%py3_build

pushd doc
    PYTHONPATH=../ sphinx-build-3 . html
    rm -fvr html/{.buildinfo,.doctrees}
popd

# Remove shebang from examples in doc
for example in examples/*.py; do
    sed '1{\@^#!/usr/bin/env python@d}' $example > $example.new &&
    touch -r $example $example.new &&
    mv $example.new $example
done

%install
%if %{with_py2}
%py2_install
%endif
%py3_install

# Remove shebang from libraries
# probably easier to use find, but the wiki suggests a for loop
%if %{with_py2}
for lib in %{buildroot}%{python2_sitelib}/%{srcname}/*.py %{buildroot}%{python2_sitelib}/%{srcname}/ext/*.py %{buildroot}%{python2_sitelib}/%{srcname}/ext/avro/*.py;
do
    echo "Working on $lib"
    sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done
%endif

for lib in %{buildroot}%{python3_sitelib}/%{srcname}/*.py %{buildroot}%{python3_sitelib}/%{srcname}/ext/*.py %{buildroot}%{python3_sitelib}/%{srcname}/ext/avro/*.py;
do
    echo "Working on $lib"
    sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done

# Ignore tests - require a hadoop cluster setup
# https://github.com/mtth/hdfs/blob/master/.travis.yml#L10

%if %{with_py2}
%files -n python2-%{srcname}
%license LICENSE
%{python2_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%{python2_sitelib}/%{srcname}/
%endif

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}*

%files doc
%doc examples AUTHORS CHANGES README.md doc/html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.8-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.8-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.8-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.5.8-1
- Update to new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.5.6-1
- New upstream version

* Wed Jun 12 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.5.4-1
- New upstream version

* Mon May 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.5.2-2
- Add buildrequire
- Fix readme extension

* Mon May 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.5.2-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-7
- Disable py2 on F30+
- Use py3 sphinx for document generation

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-5
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-2
- Fix doc generation
- Fix summary macro
- List binary files

* Mon Jan 15 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.0-1
- Initial build

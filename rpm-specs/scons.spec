# SCons 3.0.* does not run under (3.0.0) < Python3 < (3,5,0) or Python < (2,7,0).
# Epel7 provides Python3.6
# Fedora provides Python3.7 and Python3.8

%if 0%{?rhel} && 0%{?rhel} >= 8
%global with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} == 7
%global with_python3 1
%global with_python2 1
%endif

%if 0%{?fedora} && 0%{?fedora} < 32
%global with_python3 1
%global with_python2 1
%endif

%if 0%{?fedora} && 0%{?fedora} >= 32
%global with_python3 1
%endif

Name:      scons
Version:   3.1.2
Release:   3%{?dist}
Summary:   An Open Source software construction tool
License:   MIT
URL:       http://www.scons.org
Source0:   https://github.com/SCons/scons/archive/%{version}/scons-%{version}.tar.gz
Source1:   https://scons.org/doc/production/scons-doc-%{version}.tar.gz
BuildArch: noarch

%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%package doc
Summary: An Open Source software construction tool
BuildArch: noarch
%description doc
Scons HTML documentation.

%if 0%{?with_python2}
%package -n     python2-%{name}
Summary: An Open Source software construction tool

BuildRequires: python2-devel
%{?python_provide:%python_provide python2-%{name}}
%if 0%{?rhel} && 0%{?rhel} == 7
Provides:      scons = 0:%{version}-%{release}
BuildRequires: python-lxml
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
Provides:      scons-python2 = 0:%{version}-%{release}
BuildRequires: python2-lxml
%endif

%description -n python2-%{name}
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.
%endif

%if 0%{?with_python3}
%package -n     python%{python3_pkgversion}-%{name}
Summary: An Open Source software construction tool

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-lxml
%if 0%{?fedora} || 0%{?rhel} > 7
Provides:      scons = 0:%{version}-%{release}
Provides:      scons-python3
Obsoletes:     scons < 0:5.0.3-3
%endif
%if 0%{?rhel}
Obsoletes:     python34-%{name}
Provides:      scons-python3 = 0:%{version}-%{release}
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name}
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.
%endif

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{name}
Summary: An Open Source software construction tool

BuildRequires: python%{python3_other_pkgversion}-devel
BuildRequires: python%{python3_other_pkgversion}-lxml
Provides:      scons-%{__python3_other} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{name}}

%description -n python%{python3_other_pkgversion}-%{name}
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.
%endif

%prep
%setup -qc -a 1

# Remove unused doc directories
rm -rf PDF PS EPUB TEXT

# Convert to UTF-8
for file in %{name}-%{version}/src/*.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%if 0%{?with_python3}
cp -a %{name}-%{version} %{name}-%{version}-py3
%endif
%if 0%{?with_python3_other}
cp -a %{name}-%{version} %{name}-%{version}-py%{python3_other_pkgversion}
%endif
%if 0%{?with_python2}
sed -i 's|/usr/bin/env python|%{__python2}|' %{name}-%{version}/bootstrap.py
sed -i 's|/usr/bin/env python|%{__python2}|' %{name}-%{version}/src/script/*.py
%endif
%if 0%{?with_python3}
pathfix.py -i %{__python3} -pn %{name}-%{version}-py3/bootstrap.py
pathfix.py -i %{__python3} -pn  %{name}-%{version}-py3/src/script/*.py
%endif
%if 0%{?with_python3_other}
pathfix.py -i %{__python3_other} -pn %{name}-%{version}-py%{python3_other_pkgversion}/bootstrap.py
pathfix.py -i %{__python3_other} -pn %{name}-%{version}-py%{python3_other_pkgversion}/src/script/*.py
%endif

%build
%if 0%{?with_python3}
pushd %{name}-%{version}-py3
%{__python3} bootstrap.py --bootstrap_dir=build/scons
popd
%endif
%if 0%{?with_python2}
pushd %{name}-%{version}
%{__python2} bootstrap.py --bootstrap_dir=build/scons
popd
%endif
%if 0%{?with_python3_other}
pushd %{name}-%{version}-py%{python3_other_pkgversion}
%{__python3_other} bootstrap.py --bootstrap_dir=build/scons
popd
%endif

%install
%if 0%{?fedora} || 0%{?rhel} > 7
%if 0%{?with_python2}
pushd %{name}-%{version}/build/scons
%py2_install \
 --standard-lib \
 --no-install-bat \
 --no-version-script \
 --install-scripts=%{_bindir} \
 --install-data=%{_datadir}
popd

mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-2
mv %{buildroot}%{_bindir}/%{name}-configure-cache %{buildroot}%{_bindir}/%{name}-configure-cache-2
mv %{buildroot}%{_bindir}/%{name}ign %{buildroot}%{_bindir}/%{name}ign-2
mv %{buildroot}%{_bindir}/%{name}-time %{buildroot}%{_bindir}/%{name}-time-2

pushd %{buildroot}%{_bindir} 
for i in %{name}-%{python2_version} %{name}-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}-2 %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-%{python2_version} %{name}ign-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}ign-2 %{buildroot}%{_bindir}/$i
done
for i in %{name}-time-%{python2_version} %{name}-time-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}-time-2 %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-%{python2_version} %{name}-configure-cache-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}-configure-cache-2 %{buildroot}%{_bindir}/$i
done
popd
%endif
%if 0%{?with_python3}
pushd %{name}-%{version}-py3/build/scons
export LDFLAGS="%{build_ldflags}"
export CFLAGS="%{build_cflags}"
%{__python3} setup.py  install -O1 --skip-build --root %{buildroot} \
 --standard-lib \
 --no-install-bat \
 --no-version-script \
 --install-scripts=%{_bindir} \
 --install-data=%{_datadir}
rm -rfv %{buildroot}%{_bindir}/__pycache__
popd
pushd %{buildroot}%{_bindir} 
for i in %{name}-3 %{name}-v%{version}-%{python3_version} %{name}-%{python3_version}; do
  ln -fs %{_bindir}/%{name} %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-3 %{name}ign-v%{version}-%{python3_version} %{name}ign-%{python3_version}; do
  ln -fs %{_bindir}/%{name}ign %{buildroot}%{_bindir}/$i
done
for i in %{name}-time-3 %{name}-time-v%{version}-%{python3_version} %{name}-time-%{python3_version}; do
  ln -fs %{_bindir}/%{name}-time %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-3 %{name}-configure-cache-v%{version}-%{python3_version} %{name}-configure-cache-%{python3_version}; do
  ln -fs %{_bindir}/%{name}-configure-cache %{buildroot}%{_bindir}/$i
done
popd
%endif
%endif

%if 0%{?rhel} && 0%{?rhel} == 7
%if 0%{?with_python3}
pushd %{name}-%{version}-py3/build/scons
%py3_install \
 --standard-lib \
 --no-install-bat \
 --no-version-script \
 --install-scripts=%{_bindir} \
 --install-data=%{_datadir}
popd
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-3
mv %{buildroot}%{_bindir}/%{name}-configure-cache %{buildroot}%{_bindir}/%{name}-configure-cache-3
mv %{buildroot}%{_bindir}/%{name}ign %{buildroot}%{_bindir}/%{name}ign-3
mv %{buildroot}%{_bindir}/%{name}-time %{buildroot}%{_bindir}/%{name}-time-3

pushd %{buildroot}%{_bindir} 
for i in %{name}-v%{version}-%{python3_version} %{name}-%{python3_version}; do
  ln -fs %{_bindir}/%{name}-3 %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-v%{version}-%{python3_version} %{name}ign-%{python3_version}; do
  ln -fs %{_bindir}/%{name}ign-3 %{buildroot}%{_bindir}/$i
done
for i in %{name}-time-v%{version}-%{python3_version} %{name}-time-%{python3_version}; do
  ln -fs %{_bindir}/%{name}-time-3 %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-v%{version}-%{python3_version} %{name}-configure-cache-%{python3_version}; do
  ln -fs %{_bindir}/%{name}-configure-cache-3 %{buildroot}%{_bindir}/$i
done
popd
%endif
%if 0%{?with_python2}
pushd %{name}-%{version}/build/scons
%py2_install \
 --standard-lib \
 --no-install-bat \
 --no-version-script \
 --install-scripts=%{_bindir} \
 --install-data=%{_datadir}
popd
pushd %{buildroot}%{_bindir} 
for i in %{name}-2 %{name}-%{python2_version} %{name}-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name} %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-2 %{name}ign-%{python2_version} %{name}ign-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}ign %{buildroot}%{_bindir}/$i
done
for i in %{name}-time-2 %{name}-time-%{python2_version} %{name}-time-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}-time %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-2 %{name}-configure-cache-%{python2_version} %{name}-configure-cache-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}-configure-cache %{buildroot}%{_bindir}/$i
done
popd
%endif
%endif

%if 0%{?with_python3_other}
pushd %{name}-%{version}-py%{python3_other_pkgversion}/build/scons
%py3_other_install \
 --standard-lib \
 --no-install-bat \
 --no-version-script \
 --install-scripts=%{_bindir} \
 --install-data=%{_datadir}
popd

#Avoiding collisions between the python 2 and python 3 stacks
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-%{__python3_other}
mv %{buildroot}%{_bindir}/%{name}-configure-cache %{buildroot}%{_bindir}/%{name}-configure-cache-%{__python3_other}
mv %{buildroot}%{_bindir}/%{name}ign %{buildroot}%{_bindir}/%{name}ign-%{__python3_other}
mv %{buildroot}%{_bindir}/%{name}-time %{buildroot}%{_bindir}/%{name}-time-%{__python3_other}

pushd %{buildroot}%{_bindir} 
for i in %{name}-v%{version}-%{__python3_other} %{name}-%{__python3_other}; do
  ln -fs %{_bindir}/%{name}-%{__python3_other} %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-v%{version}-%{__python3_other} %{name}ign-%{__python3_other}; do
  ln -fs %{_bindir}/%{name}ign-%{__python3_other} %{buildroot}%{_bindir}/$i
done
for i in %{name}-time-v%{version}-%{__python3_other} %{name}-time-%{__python3_other}; do
  ln -fs %{_bindir}/%{name}-time-%{__python3_other} %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-v%{version}-%{__python3_other} %{name}-configure-cache-%{__python3_other}; do
  ln -fs %{_bindir}/%{name}-configure-cache-%{__python3_other} %{buildroot}%{_bindir}/$i
done
popd
%endif

%check
%if 0%{?with_python3}
pushd %{name}-%{version}-py3
%{__python3} runtest.py -P %{__python3} --passed --quit-on-failure src/engine/SCons/BuilderTests.py
popd
%endif
%if 0%{?with_python3_other}
pushd %{name}-%{version}-py%{python3_other_pkgversion}
%{__python3_other} runtest.py  -P %{__python3_other} --passed --quit-on-failure src/engine/SCons/BuilderTests.py
popd
%endif
%if 0%{?with_python2}
pushd %{name}-%{version}
%{__python2} runtest.py  -P %{__python2} --passed --quit-on-failure src/engine/SCons/BuilderTests.py
popd
%endif

%if 0%{?with_python2}
%files -n python2-%{name}
%doc %{name}-%{version}/src/CHANGES.txt %{name}-%{version}/src/README.txt %{name}-%{version}/src/RELEASE.txt
%license %{name}-%{version}/src/LICENSE.txt
%if 0%{?fedora} || 0%{?rhel} > 7
%{_bindir}/%{name}*-2
%endif
%if 0%{?rhel} && 0%{?rhel} == 7
%{_bindir}/%{name}
%{_bindir}/%{name}ign
%{_bindir}/%{name}-time
%{_bindir}/%{name}-configure-cache
%{_bindir}/%{name}*-2
%endif
%{_bindir}/%{name}*-%{python2_version}
%{python2_sitelib}/SCons/
%{python2_sitelib}/scons-%{version}*.egg-info
%{_mandir}/man?/*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{name}
%doc %{name}-%{version}-py3/src/CHANGES.txt %{name}-%{version}-py3/src/README.txt %{name}-%{version}-py3/src/RELEASE.txt
%license %{name}-%{version}-py3/src/LICENSE.txt
%if 0%{?rhel} && 0%{?rhel} == 7
%{_bindir}/%{name}*-3
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
%{_bindir}/%{name}*-3
%{_bindir}/%{name}
%{_bindir}/%{name}ign
%{_bindir}/%{name}-time
%{_bindir}/%{name}-configure-cache
%endif
%{_bindir}/%{name}*-%{python3_version}
%{python3_sitelib}/SCons/
%{python3_sitelib}/scons-%{version}*.egg-info
%{_mandir}/man?/*
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{name}
%doc %{name}-%{version}-py%{python3_other_pkgversion}/src/CHANGES.txt %{name}-%{version}-py%{python3_other_pkgversion}/src/README.txt %{name}-%{version}-py%{python3_other_pkgversion}/src/RELEASE.txt
%license %{name}-%{version}-py%{python3_other_pkgversion}/src/LICENSE.txt
%{_bindir}/%{name}*-%{__python3_other}
%{_bindir}/%{name}*-%{python3_other_pkgversion}
%{python3_other_sitelib}/SCons/
%{python3_other_sitelib}/scons-%{version}*.egg-info
%{_mandir}/man?/*
%endif

%files doc
%doc HTML
%license %{name}-%{version}/src/LICENSE.txt

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.2-3
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
- Remove missing dependencies (fop) for building doc
- %%py3_install macro is bugged

* Tue Dec 17 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2
- Use pathfix.py
- Add python-lxml lynx BR

* Fri Nov 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.1.1-4
- Fix Changelog

* Fri Nov 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.1.1-3
- Python2 SCons no longer built on Fedora 32+

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Mosaab Alzoubi <moceap@hotmail.com> - 3.1.1-1
- Update to 3.1.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.1.0-1
- Release 3.1.0

* Mon Aug 12 2019 Antonio Trande <sagitterATfedoraproject.org> - 3.0.5-5
- Provides *-3 dummy commands on Fedora and EPEL7+

* Sat Aug 03 2019 Antonio Trande <sagitterATfedoraproject.org> - 3.0.5-4
- Remove wrong links of scons-2

* Wed Jul 24 2019 Antonio Trande <sagitterATfedoraproject.org> - 3.0.5-3
- Fix builds on EPEL7

* Tue Jul 23 2019 Antonio Trande <sagitterATfedoraproject.org> - 3.0.5-2
- Unversioned commands point to Python3 on Fedora
- Obsolete Python2 version on Fedora

* Wed Mar 27 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.5-1
- Release 3.0.5

* Thu Mar 14 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.4-4
- Fix Provides of scons-python3

* Thu Mar 14 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.4-3
- Reorganize distro macros

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.0.4-1
- Release 3.0.4 (bz#1668876)

* Wed Aug 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-12
- Reintroduce python2-scons on Fedora 30+

* Wed Aug 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-11
- Deprecate Python2 on Fedora 30+ and EPEL 8+
- Use python3_other macros (https://fedoraproject.org/wiki/User:Bkabrda/EPEL7_Python3)

* Fri Jul 20 2018 Honza Horak <hhorak@redhat.com> - 3.0.1-10
- Do not build python2-scons on RHEL>7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Merlin Mathesius <mmathesi@redhat.com> - 3.0.1-6
- Cleanup spec file conditionals

* Mon Dec 25 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-5
- Remove 'Obsoletes scons' for scons-python3

* Mon Dec 25 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-4
- Fix Provides tag

* Mon Dec 25 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-3
- Set Obsoletes tag

* Mon Dec 25 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-2
- Provide Python2 and Python3 scons
- Avoiding collisions between the Python 2 and Python 3 stacks

* Tue Nov 28 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1
- Build with Python2 on EPEL7

* Tue Oct 03 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.1-1
- Update to new upstream version 3.0.0 (rhbz#1497891)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.1-1
- Update to new upstream version 2.5.1 (rhbz#1391798)

* Mon Jun 13 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.0-1
- Update to new upstream version 2.5.0

* Sat May 07 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.1-1
- Update to new upstream version 2.4.1 (rhbz#1265037)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 01 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.6-1
- Update to new upstream version 2.3.6 (rhbz#1234119)

* Wed Jul 22 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.5-1
- Update to new upstream version 2.3.5 (rhbz#1234119)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 30 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.4-1
- Update to new upstream version 2.3.4 (rhbz#1147461)

* Mon Sep 01 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.3-1
- Update to new upstream version 2.3.3 (rhbz#1133527)

* Mon Jul 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.2-1
- Update to new upstream version 2.3.2 (rhbz#1116635)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.1-1
- Update to new upstream version 2.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-1
- Update to new upstream version 2.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to new upstream version 2.2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 10 2011 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to new upstream version 2.1.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Chen Lei <supercyper@163.com> - 2.0.1-1
- new release 2.0.1

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.0-2.final.0
- recompiling .py files against Python 2.7 (rhbz#623357)

* Thu Jul 08 2010 Chen Lei <supercyper@163.com> - 2.0.0-1.final.0
- new release 2.0.0.final.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 25 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.0-1
- Update to 1.2.0 to fix problems with Python 2.6 (#475903)
  (currently causing broken deps with other packages)

* Thu Dec 18 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.1.0-1
- new release 1.1.0

* Fri Sep  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.0-1.d20080826
- new release 1.0.0

* Sun Aug  3 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.5-1
- new release 0.98.5

* Sun Jun  1 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.4-2
- added buildreq sed

* Sat May 31 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.4-1
- new release 0.98.4

* Sun May  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.3-2
- changed shebang line of scripts

* Sun May  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.3-1
- new release 0.98.3

* Sat Apr 19 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.1-1
- new release 0.98.1

* Sat Apr  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98-1
- new release 0.98

* Mon May 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.97-1
- new version 0.97

* Thu May 10 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.96.96-1
- new version 0.96.96

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.96.1-3
- Rebuild for FE6

* Sat Jun 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.96.1-1
- New Version 0.96.1

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Jan 25 2005 Thorsten Leemhuis <fedora@leemhuis.info> - 0.96-4
- Place libs in {_prefix}/lib/ and not in {libdir}; fixes x86_64 problems
- Adjust minor bits to be in sync with python-spec-template

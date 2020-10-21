%global shortname uranium-lulzbot

Name:		python-%{shortname}
Version:	3.6.21
Release:	4%{?dist}
Summary:	A Python framework for building desktop applications (Lulzbot fork)
# UM/SortedList.py is ASL 2.0
# Everything else is AGPLv3+
License:	AGPLv3+ and ASL 2.0
URL:		https://code.alephobjects.com/diffusion/U/repository/master/
# git clone https://code.alephobjects.com/diffusion/U/uranium.git
# cd uranium
# git checkout v3.6.21
## CANNOT use git archive here, because we need to scrape the hash for version
# cd ..
# mv uranium %%{shortname}-%%{version}
# tar cvfz %%{shortname}-%%{version}.tar.gz %%{shortname}-%%{version}
Source0:	%{shortname}-%{version}.tar.gz

# Cannot conflict
Patch1:		%{shortname}-3.2.17-system.patch
# Fix tests
Patch2:		%{shortname}-3.2.17-fix-test.patch

BuildRequires:	python3-devel
BuildRequires:	/usr/bin/doxygen
BuildRequires:	/usr/bin/msgmerge
BuildRequires:	cmake
BuildRequires:	git

# Tests
BuildRequires:	python3-arcus >= 3.6
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy
BuildRequires:	python3-qt5
BuildRequires:	python3-pytest

BuildArch:	noarch

# There are Python plugins in /usr/lib/uranium
# We need to byte-compile it with Python 3
%global __python %{__python3}

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%description
Uranium is a Python framework for building 3D printing related applications.

%package -n python3-%{shortname}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{shortname}}
Requires:	python3-arcus >= 3.6.0
Requires:	python3-numpy
Requires:	python3-scipy
Requires:	python3-qt5
Recommends:	python3-numpy-stl

%description -n python3-%{shortname}
Uranium is a Python framework for building 3D printing related applications.
This is the Lulzbot fork.

%package doc
Summary: Documentation for %{name} package

%description doc
Documentation for Uranium, a Python framework for building 3D printing
related applications. This is for the Lulzbot fork.

%prep
%setup -q -n %{shortname}-%{version}
%patch1 -p1 -b .system
%patch2 -p1 -b .fixtest

GITHASH=`git rev-parse HEAD`

cat > version.json << EOF
{
  "uranium": "$GITHASH"
}
EOF

# Upstream installs to lib/python3/dist-packages
# We want to install to %%{python3_sitelib}
sed -i 's|lib/python${PYTHON_VERSION_MAJOR}/dist-packages|%(echo %{python3_sitelib} | sed -e s@%{_prefix}/@@)|g' CMakeLists.txt

# Invalid locale name ptbr
# https://github.com/Ultimaker/Uranium/issues/246
mv resources/i18n/{ptbr,pt_BR}
sed -i 's/"Language: ptbr\n"/"Language: pt_BR\n"/' resources/i18n/pt_BR/*.po

# empty file. appending to the end to make sure we are not overriding
# a non empty file in the future
echo '# empty' >> UM/Settings/ContainerRegistryInterface.py

%build
%cmake
%cmake_build
%cmake_build -- doc

%install
%cmake_install

# Move the cmake files
mv %{buildroot}%{_datadir}/cmake* %{buildroot}%{_datadir}/cmake

# remove conflict
mv %{buildroot}%{_datadir}/cmake/Modules/UraniumTranslationTools.cmake %{buildroot}%{_datadir}/cmake/Modules/LulzbotUraniumTranslationTools.cmake

# Sanitize the location of locale files
pushd %{buildroot}%{_datadir}
mv %{shortname}/resources/i18n locale
ln -s ../../locale %{shortname}/resources/i18n
rm locale/uranium.pot
rm locale/*/uranium.po
for i in locale/*/LC_MESSAGES; do
	pushd $i
	mv uranium.mo %{shortname}.mo
	popd
done
popd

cp version.json %{buildroot}%{_datadir}/%{shortname}/

# Bytecompile the plugins
%py_byte_compile %{__python3} %{buildroot}%{_prefix}/lib/%{shortname}

%find_lang %{shortname}

%check
# test code now tries to load cura, which we don't want as a dep, since it makes a loop
%if 0
pip3 freeze

# The failing tests are reported at:
# https://github.com/Ultimaker/Uranium/issues/225
# Skipping
%{__python3} -m pytest -v -k "not getMimeTypeForFile"
%endif

%files -n python3-%{shortname} -f %{shortname}.lang
%license LICENSE
%doc README.md
%dir %{python3_sitelib}/CuraLulzbot
%{python3_sitelib}/CuraLulzbot/UM
%{_datadir}/%{shortname}
# Own the dir not to depend on cmake:
%{_datadir}/cmake
%{_prefix}/lib/%{shortname}

%files doc
%license LICENSE
%doc html

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.21-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.21-1
- update to 3.6.21

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.18-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.18-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.18-1
- update to 3.6.18

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.12-1
- update to 3.6.12

* Tue May 14 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.8-2
- fix issue where qt5.12 does not properly identify function objects that results
  in all internationalized strings not rendering (bz1708956)

* Thu May  2 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.8-1
- update to 3.6.8

* Thu Apr 18 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.6-1
- update to 3.6.6

* Wed Apr 17 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.5-2
- fix arcus requirements

* Wed Mar 27 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.5-1
- update to 3.6.5

* Wed Feb 20 2019 Tom Callaway <spot@fedoraproject.org> - 3.6.3-1
- update to 3.6.3

* Fri Nov 16 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.32-1
- update to 3.2.32

* Mon Jul 30 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.23-1
- update to 3.2.23

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.21-2
- Rebuilt for Python 3.7

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.21-1
- update to 3.2.21

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.20-1
- update to 3.2.20

* Wed May  9 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.19-1
- update to 3.2.19

* Mon Apr 23 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.18-1
- update to 3.2.18

* Mon Apr 16 2018 Tom Callaway <spot@fedoraproject.org> - 3.2.17-1
- update to 3.2.17

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 2.6.69-1
- update to 2.6.69

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Tom Callaway <spot@fedoraproject.org> - 2.6.66-1
- update to 2.6.66

* Thu Jan 11 2018 Tom Callaway <spot@fedoraproject.org> - 2.6.63-3
- use shortname macro consistently

* Wed Jan 10 2018 Tom Callaway <spot@fedoraproject.org> - 2.6.63-2
- add explicit text to summaries/descriptions to make clear this is a fork
- own %%{python3_sitelib}/CuraLulzbot
- correct license tag
- rename translation files to avoid conflict

* Wed Jan  3 2018 Tom Callaway <spot@fedoraproject.org> - 2.6.63-1
- update to 2.6.63

* Fri Dec  8 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.52-1
- update to 2.6.52

* Fri Oct 27 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.43-1
- update to 2.6.43

* Fri Oct 27 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.29-1
- update to 2.6.29

* Wed Aug 23 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.23-1
- update to 2.6.23

* Wed Aug 16 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.22-2
- fix python 3 version hardcoding in patch

* Mon Aug 14 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.22-1
- update to 2.6.22

* Tue Aug  8 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.21-2
- fix namespacing (thanks to Miro Hrončok)

* Tue Aug  8 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.21-1
- update to 2.6.21

* Thu Jul 27 2017 Tom Callaway <spot@fedoraproject.org> - 2.6.19-1
- make lulzbot specific package

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-2
- Fix the test_uniqueName test failure

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-1
- Update to 2.6.1
- Skip test_uniqueName test (reported)

* Tue Jun 27 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Actually include the cmake files (needed for cura)

* Wed Apr 26 2017 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Initial package


# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           otf2
Version:        2.2
Release:        10%{?dist}
Summary:        Open Trace Format 2 library

License:        BSD
URL:            http://score-p.org
Source0:        https://www.vi-hps.org/cms/upload/packages/otf2/%{name}-%{version}.tar.gz
# fedpkg new-sources apparently can't cope with both otf2-1.5.1 and
# otf2-2.2 tarballs.
%{?el7:Source1:        https://www.vi-hps.org/cms/upload/packages/otf2/otf2-1.5.1.tar.gz}
# Remove jinja2
Patch0:         otf2-jinja2.patch
# Avoid -rpath in otf2-config output
Patch1:         otf2-rpath.patch
# Fix AC_CONFIG_MACRO_DIR and remove $(srcdir) from TESTS
%{?el7:Patch3:         otf2-autoconf.patch}
BuildRequires:  gcc-c++
BuildRequires:  chrpath dos2unix
BuildRequires:  libtool automake


%description
The Open Trace Format 2 (OTF2) is a highly scalable, memory efficient
event trace data format plus support library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Development files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation files for %{name}.

# Python packages can't be noarch as they require arch-specific otf2
%if %{with python2}
%package -n python2-otf2
Summary:        Python 2 bindings for %{name}
BuildRequires:  python2-devel
BuildRequires:  python2-six
Requires:       python2-jinja2 python2-six python2-future
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python2-otf2
Python 2 bindings for %{name}.
%endif

%package -n python%{python3_pkgversion}-otf2
Summary:        Python 3 bindings for %{name}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-jinja2 python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-future
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python%{python3_pkgversion}-otf2
Python 3 bindings for %{name}.

%if 0%{?el7}
%package compat
Summary:        Compatibility library for %name version 1.

%description compat
Compatibility library for %name version 1.
%endif

%prep
%setup -q
%patch0 -p1 -b .jinja2
%patch1 -p1 -b .rpath
# Bundled modified jinja2 in vendor/
rm -r vendor/python/site-packages
autoreconf -fiv
# Remove ldflags
sed -i -s '/deps.GetLDFlags/d' src/tools/otf2_config/otf2_config.cpp
dos2unix doc/examples/otf2_high_level_writer_example.py
%if 0%{?el7}
tar fx %SOURCE1
cd otf2-1.5.1
%patch3 -p1
for d in . build-backend build-frontend
do
  cd $d
  autoreconf -f -i -v
  cd -
done
%endif

%build
export PYTHON_FOR_GENERATOR=:
%configure --disable-static --enable-shared --disable-silent-rules \
 --docdir=%{_pkgdocdir} --enable-backend-test-runs --with-platform=linux
%make_build
%if 0%{?el7}
pushd otf2-1.5.1
%configure --disable-static --enable-shared --disable-silent-rules \
 --docdir=%{_pkgdocdir} --with-platform=linux
%make_build
popd
%endif


%install
%make_install
find %{buildroot} -name '*.la' -delete
cp -p AUTHORS ChangeLog README %{buildroot}%{_pkgdocdir}/
chrpath -d %{buildroot}%{_bindir}/otf2-{marker,print,snapshots,estimator,config}
rm %{buildroot}%{_pkgdocdir}/python/.buildinfo
%if %{with python2}
mkdir -p %{buildroot}%{python2_sitelib}
cp -a %{buildroot}%{_datadir}/%{name}/python %{buildroot}%{python2_sitelib}/%{name}
%endif
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{_datadir}/%{name}/python %{buildroot}%{python3_sitelib}/%{name}
%if 0%{?el7}
%make_install -C otf2-1.5.1 DESTDIR=$(pwd)/otf2-1.5.1
cp -a otf2-1.5.1%{_libdir}/libotf2.so.5* %{buildroot}%{_libdir}
%endif


%check
make check


%ldconfig_scriptlets
%ldconfig_scriptlets compat


%files
%license COPYING
%{_bindir}/%{name}-estimator
%{_bindir}/%{name}-marker
%{_bindir}/%{name}-print
%{_bindir}/%{name}-snapshots
%{_libdir}/lib%{name}.so.7*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/%{name}.summary
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/OPEN_ISSUES
%{_pkgdocdir}/README
%exclude %{_pkgdocdir}/html
%exclude %{_pkgdocdir}/pdf
%exclude %{_pkgdocdir}/tags

%files devel
%{_bindir}/%{name}-config
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files doc
%license COPYING
%dir %{_pkgdocdir}
%{_pkgdocdir}/examples/
%{_pkgdocdir}/html/
%{_pkgdocdir}/pdf/
%{_pkgdocdir}/tags/
%{_pkgdocdir}/python/

%files -n python%{python3_pkgversion}-otf2
%{python3_sitelib}/%{name}/
%{python3_sitelib}/_%{name}/

%if %{with python2}
%files -n python2-otf2
%{python2_sitelib}/%{name}/
%{python2_sitelib}/_%{name}/
%endif

%if 0%{?el7}
%files compat
%{_libdir}/libotf2.so.5*
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2-10
- Rebuilt for Python 3.9

* Sun Feb 23 2020 Orion Poplawski <orion@nwra.com> - 2.2-9
- Drop python2 for EL8
- Really build python bindings

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Dave love <loveshack@fedoraproject.org> - 2.2-7
- Re-sync epel7 and rawhide for Source1

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 2.2-6
- Comment out nonexistent Source1

* Fri Jan 17 2020 Dave love <loveshack@fedoraproject.org> - 2.2-6
- Fix FTBFS due to bad el7 conditionals (#1791678)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Dave love <loveshack@fedoraproject.org> - 2.2-4
- Provide -compat package for el7

* Tue Aug 20 2019 Dave love <loveshack@fedoraproject.org> - 2.2-3
- Avoid generating otf2-template (#1738058)

* Fri Aug 16 2019 Dave love <loveshack@fedoraproject.org> - 2.2-2
- Make python2 and python3 packages (#1738058)
- Require python{2,3}-six, python{2,3}-future

* Thu Aug  1 2019 Dave love <loveshack@fedoraproject.org> - 2.2-1
- New version
- Update URLs

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Orion Poplawski <orion@nwra.com> - 2.1.1-1
- Update to 2.1.1

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Dave Love <loveshack@fedoraproject.org> - 2.1-1
- Update to 2.1
- Re-do jinja patch
- Fix line endings and use of rpath; add otf2-rpath.patch

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0-1
- Update to 2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Orion Poplawski <orion@cora.nwra.com> - 1.5.1-2
- BR autoconf268 on el6 and use it
- Do not apply autoconf patch and only autoreconf top level on el6
- Fixup doc install

* Wed Feb 11 2015 Orion Poplawski <orion@cora.nwra.com> - 1.5.1-1
- Update to 1.5.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Orion Poplawski <orion@cora.nwra.com> - 1.4-2
- Remove ldflags output from otf2-config

* Tue Jul 15 2014 Orion Poplawski <orion@cora.nwra.com> - 1.4-1
- Update to 1.4
- Add patch to allow running autoreconf to remove rpaths

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-4
- Move otf2-config back to -devel

* Mon Oct 21 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-3
- Add BR python2-devel
- Add Requires jinja2
- Exclude docs from main package
- Rebase jinja2 patch

* Wed Oct 2 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-2
- Fix rpath with configure change

* Wed Sep 25 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-1
- Initial package

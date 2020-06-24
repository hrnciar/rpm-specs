Name:           scapy
Version:        2.4.3
Release:        5%{?dist}
Summary:        Interactive packet manipulation tool and network scanner

%global         gituser         secdev
%global         gitname         scapy
%global         commit          3047580162a9407ef05fe981983cacfa698f1159
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

License:        GPLv2
URL:            http://www.secdev.org/projects/scapy/
#               https://github.com/secdev/scapy/releases
#               https://bitbucket.org/secdev/scapy/pull-request/80
#               https://scapy.readthedocs.io/en/latest/introduction.html
Source0:        https://github.com/%{gituser}/%{gitname}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://github.com/secdev/scapy/commit/0c3d5e417bbd923c4729d15572c3d693d58aff81.patch#/scapy-2.4.3-ethertypes.patch

%global         common_desc %{expand:
Scapy is a powerful interactive packet manipulation program built on top
of the Python interpreter. It can be used to forge or decode packets of
a wide number of protocols, send them over the wire, capture them, match
requests and replies, and much more.}


# By default build with python3 subpackage
%bcond_without     python3

# Build also the python2 package on releases up to fc31 and rhel8
%if (0%{?fedora} && 0%{?fedora} <= 31 ) || ( 0%{?rhel} && 0%{?rhel} <= 8 )
%bcond_without     python2
%else
%bcond_with        python2
%endif

# By default build the documentation
%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} >= 8 )
%bcond_without     doc
%else
# Documentation build fails on rhel7 due to version of sphinx
%bcond_with        doc
%endif




BuildArch:      noarch

BuildRequires:  sed

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

# Recommends only supported on fedora and rhel8+
%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
Recommends:     tcpdump
# Using database of manufactures /usr/share/wireshark/manuf
Recommends:     wireshark-cli
%endif

%description %{common_desc}

%if 0%{?with_python2}
%package -n python2-%{name}
Summary:        Interactive packet manipulation tool and network scanner

%{?python_provide:%python_provide python2-%{name}}

%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 ) 
Recommends:     python2-pyx
Recommends:     python2-matplotlib
Recommends:     ipython2
%endif

%description -n python2-%{name}
%{common_desc}

%endif


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{name}
Summary:        Interactive packet manipulation tool and network scanner

%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Provides:       %{name} = %{version}-%{release}

%if (0%{?fedora}) || ( 0%{?rhel} && 0%{?rhel} >= 8 ) 
Recommends:     PyX
Recommends:     python%{python3_pkgversion}-matplotlib
Recommends:     ipython3
%endif

%description -n python%{python3_pkgversion}-%{name}
%{common_desc}
%endif

%if 0%{?with_doc}
%package doc
Summary:        Interactive packet manipulation tool and network scanner

BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme

%description doc
%{common_desc}
%endif



%prep
%autosetup -p 1 -n %{name}-%{version}

# Remove shebang
# https://github.com/secdev/scapy/pull/2332
SHEBANGS=$(find ./scapy -name '*.py' -print | xargs grep -l -e '^#!.*env python')
for FILE in $SHEBANGS ; do
    sed -i.orig -e 1d "${FILE}"
    touch -r "${FILE}.orig" "${FILE}"
    rm "${FILE}.orig"
done



%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?with_doc}
make -C doc/scapy html BUILDDIR=_build_doc SPHINXBUILD=sphinx-build-%python3_version

rm -f doc/scapy/_build_doc/html/.buildinfo
rm -f doc/scapy/_build_doc/html/_static/_dummy
%endif



%install
install -dp -m0755 %{buildroot}%{_mandir}/man1
install -Dp -m0644 doc/scapy.1* %{buildroot}%{_mandir}/man1/

%if 0%{?with_python2}
%py2_install
rm -f %{buildroot}%{python2_sitelib}/*egg-info/requires.txt


# Rename the executables
mv -f %{buildroot}%{_bindir}/scapy   %{buildroot}%{_bindir}/scapy2
mv -f %{buildroot}%{_bindir}/UTscapy %{buildroot}%{_bindir}/UTscapy2

%if ! 0%{?with_python3}
# Link the default to the py2 version of executables if py3 not built
ln -s %{_bindir}/scapy2   %{buildroot}%{_bindir}/scapy
ln -s %{_bindir}/UTscapy2 %{buildroot}%{_bindir}/UTscapy
%endif
%endif

%if 0%{?with_python3}
%py3_install
rm -f %{buildroot}%{python3_sitelib}/*egg-info/requires.txt

# Rename the executables
mv -f %{buildroot}%{_bindir}/scapy   %{buildroot}%{_bindir}/scapy3
mv -f %{buildroot}%{_bindir}/UTscapy %{buildroot}%{_bindir}/UTscapy3

# Link the default to the python3 version of executables
ln -s %{_bindir}/scapy3   %{buildroot}%{_bindir}/scapy
ln -s %{_bindir}/UTscapy3 %{buildroot}%{_bindir}/UTscapy
%endif



# check
# TODO: Need to fix/remove slow/failed test
# cd test/
# ./run_tests_py2 || true
# ./run_tests_py3 || true



%if 0%{?with_python2}
%files -n python2-%{name}
%license LICENSE
%if ! 0%{?with_python3}
%doc %{_mandir}/man1/scapy.1*
%{_bindir}/scapy
%{_bindir}/UTscapy
%endif
%{_bindir}/scapy2
%{_bindir}/UTscapy2
%{python2_sitelib}/scapy/
%{python2_sitelib}/scapy-*.egg-info
%endif



%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{name}
%license LICENSE
%doc %{_mandir}/man1/scapy.1*
%{_bindir}/scapy
%{_bindir}/UTscapy
%{_bindir}/scapy3
%{_bindir}/UTscapy3
%{python3_sitelib}/scapy/
%{python3_sitelib}/scapy-*.egg-info
%endif


%if 0%{?with_doc}
%files doc
%doc doc/scapy/_build_doc/html
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Michal Ambroz <rebus _AT seznam.cz> - 2.4.3-3
- remove colliding manpage from python2 package
- add license files
- add doc subpackage
- remove shebangs

* Sun Oct 06 2019 Michal Ambroz <rebus _AT seznam.cz> - 2.4.3-2
- change to recommended python build dependencies for EPEL7 - thanks Miro Hroncok

* Thu Sep 26 2019 Michal Ambroz <rebus _AT seznam.cz> - 2.4.3-1
- bump to 2.4.3 release
- change the python2 to conditional build to be able to keep one spec for all
- add Recommends for dependencies, except for EPEL7

* Fri Sep 20 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-8
- Subpackage python2-scapy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.7

* Mon Apr 30 2018 Michal Ambroz <rebus _AT seznam.cz> - 2.4.0-2
- disable the test for now - there is too many failing (network) tests

* Mon Apr 30 2018 Michal Ambroz <rebus _AT seznam.cz> - 2.4.0-1
- bump to 2.4.0 release

* Fri Mar 9 2018 Michal Ambroz <rebus _AT seznam.cz> - 2.4.0-0.rc5.1
- bump to upstream 2.4.0 release candidate 5
- enable separate python3 and python2 build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Michal Ambroz <rebus _AT seznam.cz> - 2.3.3-1
- bump to upstream 2.3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Sven Lankes <athmane@fedoraproject.org> - 2.3.1-1
- update to latest upstream release (2.3.1)
- Update to 2.3.1
- Remove upstreamed patch
- Some spec fixes
- Thanks to Athmane Madjoudj for the patch

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.2.0-5
- Fix psdump()/pdfdump()

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Sven Lankes <sven@lank.es> - 2.2.0-1
- Update to Scapy 2.2.0
- Fixes rhbz #788659 - thanks to Thiébaud Weksteen

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 2.0.0.10-1
- Update to Scapy 2.0.0.10.

* Sun Dec 07 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 2.0.0.9-2
- Update for Scapy 2.0.0.9.

* Tue Jan 22 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-4
- Switch to using rm macro.

* Mon Jan 21 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-2
- Spec file cleanup.

* Fri Jan 18 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-1
- Initial packaging for Fedora.

%global owner michaeljones
%global srcname breathe
%global _description \
Breathe is an extension to reStructuredText and Sphinx to be able to read and \
render the Doxygen xml output.

Name:           python-%{srcname}
Version:        4.14.2
Release:        2%{?dist}
Summary:        Adds support for Doxygen xml output to reStructuredText and Sphinx

License:        BSD
URL:            https://github.com/%{owner}/%{srcname}
Source0:        %{URL}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  doxygen >= 1.8.4
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %{py3_dist six} >= 1.9
BuildRequires:  %{py3_dist Sphinx} >= 2.0
BuildRequires:  %{py3_dist docutils} >= 0.12
BuildRequires:  %{py3_dist pytest}
# NOTE: git is only needed because part of the build process checks if it's in
# a git repo
BuildRequires:  git

# Set the name of the documentation directory
%global _docdir_fmt %{name}

%description %_description

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-six
Requires:       doxygen >= 1.8.4
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%package        doc
Summary:        Documentation files for %{srcname}
# tinyxml uses zlib license
License:        BSD and zlib

%description    doc
This package contains documentation for developer documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
# Build the documentation
make %{?_smp_mflags} DOXYGEN=$(which doxygen) html
# Remove temporary build files
rm documentation/build/html/.buildinfo

%install
%py3_install

%check
make dev-test

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%{_bindir}/breathe-apidoc
%{python3_sitelib}/*
%license LICENSE

%files doc
%doc documentation/build/html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.14.2-2
- Rebuilt for Python 3.9

* Wed Apr  8 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 4.14.2-1
- New upstream release 4.14.2

* Sun Feb  2 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 4.14.1-1
- New upstream release 4.14.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 4.14.0-1
- New upstream release 4.14.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.13.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 4.13.1-1
- New upstream release 4.13.1
- Enable test run in %%check

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.13.0.post0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.0.post0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 4.13.0.post0-1
- New upstream release 4.13.0.post0

* Mon Mar 18 2019 Miro Hrončok <mhroncok@redhat.com> - 4.7.3-7
- Subpackage python2-breathe has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.7.3-4
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.7.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Dave Johansen <davejohansen@gmail.com> - 4.7.3-1
- Upstream update

* Tue Aug 22 2017 Dave Johansen <davejohansen@gmail.com> - 4.7.2-1
- Upstream update

* Wed Aug 16 2017 Dave Johansen <davejohansen@gmail.com> - 4.7.1-1
- Upstream update

* Wed Aug 09 2017 Dave Johansen <davejohansen@gmail.com> - 4.7.0-1
- Upstream update

* Sat Aug 05 2017 Dave Johansen <davejohansen@gmail.com> - 4.6.0-3
- Fix for node without parent

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-1
- Upstream update

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Dave Johansen <davejohansen@gmail.com> - 4.4.0-1
- Upstream release

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 13 2016 Dave Johansen <davejohansen@gmail.com> - 4.2.0-3
- Fix for Python 3

* Sun Apr 10 2016 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-2
- Fix BR/Rs

* Wed Apr 06 2016 Dave Johansen <davejohansen@gmail.com> - 4.2.0-1
- Initial RPM release
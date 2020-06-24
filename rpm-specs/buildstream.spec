Name:          buildstream
Summary:       Build/integrate software stacks
License:       LGPLv2+
URL:           https://buildstream.gitlab.io/buildstream/

Version:       1.4.1
Release:       3%{?dist}
Source0:       https://gitlab.com/BuildStream/buildstream/-/archive/%{version}/buildstream-%{version}.tar.bz2

BuildRequires: bubblewrap >= 0.1.2
BuildRequires: python3-devel >= 3.5
BuildRequires: python3-pylint
BuildRequires: python3-pytest >= 3.7
BuildRequires: python3-pytest-runner
BuildRequires: python3-pytest-timeout
BuildRequires: python3-pytest-xdist
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-click
BuildRequires: python3-sphinx_rtd_theme

# These aren't in Fedora any more, preventing us from running the tests.
# Buildstream master moved to pycodestyle though, so this will sort itself out.
#BuildRequires: python3-pep8
#BuildRequires: python3-pytest-pep8

# These aren't in Fedora yet, preventing us from running the tests
#BuildRequires: python3-pytest-datafiles
#BuildRequires: python3-pytest-env
#BuildRequires: python3-pytest-pylint

# Runtime deps, required to build the docs and run the tests
BuildRequires: fuse-libs
BuildRequires: ostree-libs
BuildRequires: python3-arpy
BuildRequires: python3-click
BuildRequires: python3-gobject
BuildRequires: python3-grpcio >= 1.10
BuildRequires: python3-jinja2 >= 2.10
BuildRequires: python3-pluginbase
BuildRequires: python3-protobuf >= 3.5
BuildRequires: python3-psutil
BuildRequires: python3-ruamel-yaml >= 0.16
BuildRequires: python3-ujson

Requires:      bubblewrap
Requires:      fuse-libs
Requires:      git
Requires:      lzip
Requires:      ostree-libs
Requires:      patch
Requires:      python3-arpy
Requires:      python3-click
Requires:      python3-gobject
Requires:      python3-grpcio >= 1.10
Requires:      python3-jinja2 >= 2.10
Requires:      python3-pluginbase
Requires:      python3-protobuf >= 3.5
Requires:      python3-psutil
Requires:      python3-ruamel-yaml >= 0.16
Requires:      python3-setuptools
Requires:      python3-ujson
Requires:      tar

BuildArch:     noarch

%description
BuildStream is a Free Software tool for building/integrating software stacks.
It takes inspiration, lessons and use-cases from various projects including
OBS, Reproducible Builds, Yocto, Baserock, Buildroot, Aboriginal, GNOME
Continuous, JHBuild, Flatpak Builder and Android repo.

BuildStream supports multiple build-systems (e.g. autotools, cmake, cpan,
distutils, make, meson, qmake), and can create outputs in a range of formats
(e.g. debian packages, flatpak runtimes, sysroots, system images) for multiple
platforms and chipsets.


%package docs
Summary:       BuildStream documentation

%description docs
BuildStream is a Free Software tool for building/integrating software stacks.
It takes inspiration, lessons and use-cases from various projects including
OBS, Reproducible Builds, Yocto, Baserock, Buildroot, Aboriginal, GNOME
Continuous, JHBuild, Flatpak Builder and Android repo.

BuildStream supports multiple build-systems (e.g. autotools, cmake, cpan,
distutils, make, meson, qmake), and can create outputs in a range of formats
(e.g. debian packages, flatpak runtimes, sysroots, system images) for multiple
platforms and chipsets.

This package provides the documentation for BuildStream.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%py3_build

pushd doc
make devhelp
popd


%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/gtk-doc/html/
cp -pr doc/build/devhelp %{buildroot}%{_datadir}/gtk-doc/html/BuildStream


# Disable the tests for now, too many unavailable dependencies
%check
#%%{__python3} setup.py test


%files
%doc NEWS README.rst
%license COPYING
%{_bindir}/bst*
%{python3_sitelib}/BuildStream-%{version}*.egg-info
%{python3_sitelib}/buildstream
%{_datadir}/bash-completion/completions/bst
%{_mandir}/man1/bst*


%files docs
%{_datadir}/gtk-doc


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Mathieu Bridon <bochecha@daitauha.fr> - 1.4.1-1
- Update to the latest upstream release.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.8-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.8-1
- Update to the latest upstream release.

* Tue May 21 2019 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.7-1
- Update to the latest upstream release.

* Thu May 02 2019 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.6-1
- Update to the latest upstream release.

* Mon Apr 22 2019 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.5-1
- Update to the latest upstream release.

* Thu Feb 14 2019 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.4-1
- Update to the latest upstream release.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.3-3
- Rebuild with the new release tarball
  https://gitlab.com/BuildStream/buildstream/issues/820
- Remove brackets around command macros, to avoid future annoyance if I add
  arguments to them.

* Mon Dec 17 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.3-2
- Make buildstream work with click 7.

* Fri Oct 05 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.3-1
- Update to the latest upstream release.

* Mon Sep 24 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.2-1
- Update to the latest upstream release.

* Sun Sep 23 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.1-2
- Add back the blessings dependency.
  https://gitlab.com/BuildStream/buildstream/merge_requests/821

* Fri Sep 21 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.1-1
- Update to the latest upstream release.

* Mon Sep 03 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.0-1
- Update to the latest upstream release.

* Fri Aug 24 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.1.7.1
- Update to the latest upstream release.

* Tue Aug 14 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.1.6-2
- Set the minimum required version of python3-blessings.
  https://gitlab.com/BuildStream/buildstream/merge_requests/663

* Tue Aug 14 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.1.6-1
- Update to the latest upstream release.

* Mon Aug 06 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.1.5-1
- Update to the latest upstream release.
- Add some optional dependencies.

* Sat Aug 04 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.1.4-1
- Initial package for fedora.

Name:           python-deap
Version:        1.3.1
Release:        3%{?dist}
Summary:        Distributed Evolutionary Algorithms in Python

License:        LGPLv3
URL:            https://www.github.com/deap
Source0:        %{pypi_source}

# Fixes error "Reason: TemplateNotFound()"
Patch1:         remove-sidebar.diff

BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pypandoc
BuildRequires:  python3-nose
BuildRequires:  python3-numpy

# documentation
BuildRequires:  python3-sphinx
BuildRequires:  texlive-scheme-basic
BuildRequires:  tex(ucs.sty)
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  python3-numpy
BuildRequires:  python3-matplotlib

%global _description %{expand:
DEAP is a novel evolutionary computation framework for rapid
prototyping and testing of ideas that implements a number of genetic
optimization algorithms behind a common interface.}

%description %_description

%package -n     python3-deap
Requires:       python3-numpy
Summary:        %{summary}
%{?python_provide:%python_provide python3-deap}

%description -n python3-deap %_description

%package -n python-deap-doc
Summary:        Documentation for deap
BuildArch:      noarch
%description -n python-deap-doc
%{summary}.

%prep
%autosetup -n deap-%{version} -p1
sed -i 's/\["git", "rev-parse", "HEAD"\]/["echo", "deap-%{version}-%{release}"]/' \
    doc/conf.py

2to3 -nw doc/conf.py

# # Work around for https://github.com/matplotlib/matplotlib/issues/7313
# sed -i -r 's/arange\(([-0-9.]+), ([-0-9.]+), [-0-9.]+\)/linspace(\1, \2, 20)/' doc/code/benchmarks/*.py

# https://bugzilla.redhat.com/show_bug.cgi?id=1644771
sed -i -r "s|'matplotlib.sphinxext.only_directives',||" doc/conf.py

%build
%py3_build

# generate html docs
PYTHONPATH=build/lib.%{python3_platform}-%{python3_version} sphinx-build-3 doc build/html

# remove the sphinx-build leftovers
rm -rf build/html/.{doctrees,buildinfo}

%global _docdir_fmt %{name}

%install
%py3_install

%check
%ifarch s390x
# Fails with: AssertionError: CMA algorithm did not converged properly.
%global test_options --exclude test_cma
%endif

%{__python3} setup.py nosetests %{?test_options}

%files -n python3-deap
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/deap
%{python3_sitearch}/deap-*.egg-info

%files -n python-deap-doc
%license LICENSE.txt
%doc build/html

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 1.3.1-1
- Version update to 1.3.1
- New version fixes fails to build with Python 3.9: imports abc from collections (#1792065)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.0-1
- Update to 1.3.0 (#1514435)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-14.20160624git232ed17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13.20160624git232ed17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-12.20160624git232ed17
- Fix build with sphinx 2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11.20160624git232ed17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-10.20160624git232ed17
- Subpackage python2-deap has been removed (#1630955)
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
- Remove use of only_directives sphinx extension to fix build (#1606870)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9.20160624git232ed17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8.20160624git232ed17
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7.20160624git232ed17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-6.20160624git232ed17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5.20160624git232ed17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4.20160624git232ed17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3.20160624git232ed17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Adam Williamson <awilliam@redhat.com> - 1.0.1-2.20160624git232ed17
- Tweak setup.py so Python 3 tests will run on 2to3'ed code
- Add appropriate buildrequires and enable tests
- Remove some unneeded conditionals for EOL Fedora releases

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Oct 18 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-1.20160624git232ed17
- Update to latest git snapshot
- The version was wrong (upstream never released anything after
  1.0.1).  I forgot to actually create an update with the initial
  version of this package. Luckily, this package was only built in
  F22-24, and failed to build in rawhide, so it was never possible to
  install it from repositories. I think this means it is possible to
  lower the version without bumping the epoch.

* Thu Apr 07 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.10-0.20160402gita4dc752
- Initial package.

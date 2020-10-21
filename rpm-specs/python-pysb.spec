# Documentation cannot be built on epel7, python-numpydoc is missing
%global with_doc  0%{?fedora}

# Use the same directory of the main package for subpackage licence and doc
%global _docdir_fmt %{name}

Name:           python-pysb
Version:        1.11.0
Release:        4%{?dist}
Summary:        Rule-based modeling of biochemical systems as Python programs
License:        BSD
URL:            http://pysb.org/
Source0:        %{pypi_source pysb}
BuildArch:      noarch

BuildRequires:  perl-macros
BuildRequires:  python3-devel
BuildRequires:  python3-nose
# For building documentation
%if %{with_doc}
BuildRequires:  dvipng
BuildRequires:  python3-sphinx
BuildRequires:  tex(latex)
BuildRequires:  python3-numpydoc
%endif

%global _description %{expand:
PySB is a framework for building mathematical models of biochemical
systems as Python programs. PySB abstracts the complex process of
creating equations describing interactions among multiple proteins or
other biomolecules into a simple and intuitive domain specific
programming language, which is internally translated into BioNetGen or
Kappa rules and from there into systems of equations. PySB makes it
straightforward to divide models into modules and to call libraries of
reusable elements (macros) that encode standard biochemical
actions. These features promote model transparency, reuse and
accuracy. PySB also interoperates with standard scientific Python
libraries such as NumPy, SciPy and SymPy enabling model simulation and
analysis.}

%description %_description

%package -n python3-pysb
Summary: %summary
Requires:       bionetgen
Requires:       bionetgen-perl
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-matplotlib
Requires:       python3-sympy
Requires:       python3-pygraphviz
Requires:       python3-networkx
%{?python_provide:%python_provide python3-pysb}

%description -n python3-pysb %_description

%if %{with_doc}
%package doc
Summary:        HTML documentation for %{name}
Requires:       python3-pysb = %{version}-%{release}
BuildRequires:  python3-mock
Provides:       bundled(jquery)
Obsoletes:      %{name}-docs <= 1.0.1

%description doc
This package contains HTML documentation for %{name}.
%endif

%prep
%setup -q -n pysb-%{version}
# https://github.com/pysb/pysb/issues/100
sed -i -e "s|/usr/local/share/BioNetGen|%{perl_vendorlib}/BioNetGen|" \
       -e "s|'c:/Program Files/BioNetGen',||" \
    pysb/bng.py
sed -i -s "1 s|/usr/bin/env python|%{__python3}|" pysb/examples/*.py pysb/tools/*.py

%build
%py3_build

# Build documentation
%if %{with_doc}
make -C doc html
rm doc/_build/html/.buildinfo
%endif

%install
%py3_install
chmod +x %{buildroot}/%{python3_sitelib}/pysb/examples/run_*.py
chmod +x %{buildroot}/%{python3_sitelib}/pysb/tools/[a-z]*.py

%files -n python3-pysb
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/pysb/
%{python3_sitelib}/pysb-%{version}-*.egg-info
%{_bindir}/pysb_export

%if %{with_doc}
%files doc
%license LICENSE.txt
%doc doc/_build/html
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019  <zbyszek@in.waw.pl> - 1.11.0-1
- Update to 1.11.0 (#1772191)

* Fri Oct 25 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.10.0-1
- Update to 1.10.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.1-1
- Update to latest version (#1708760)

* Thu Apr 11 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.8.1-1
- Update to 1.8.1
- Add missing BR

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Petr Viktorin <releng@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0
- Switch to Python 3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-8
- Python 2 binary package renamed to python2-pysb
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.0.1-5
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-1
- Update to 1.0.1
- Remove merged patches
- Rename -docs do -doc following Packaging Guidelines

* Tue Jan  6 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-1
- Update to 1.0.0 (#1178418)
- Add docs subpackage

* Wed Dec 03 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.11-2
- Fix shebangs and permissions on scripts.

* Fri Nov 21 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.11-1
- Initial packaging.

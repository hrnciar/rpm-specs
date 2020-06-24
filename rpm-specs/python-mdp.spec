%global forgeurl  https://github.com/mdp-toolkit/mdp-toolkit
%global commit 1693b65e5cad07cc3325034e6ebae4ea8ba9ce2a

%forgemeta

Name:           python-mdp
Version:        3.5
Release:        19%{?dist}
Summary:        Library for building data processing pipelines for machine learning

License:        BSD
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://github.com/mdp-toolkit/mdp-docs/archive/MDP-%{version}.tar.gz#/MDP-docs-%{version}.tar.gz
# also:         https://pypi.python.org/pypi/MDP

# not submitted upstream
Patch0:         0000-Remove-usage-of-functions-removed-from-sphinx.patch

# upstream or submitted upstream
Patch15:        0015-Fix-compatibility-with-sphinx-2.0.patch
Patch16:        0016-ext-codesnippet-remove-use-of-removed-function.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-future
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
# libsvm-python3 is missing
BuildRequires:  python3-joblib
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-pytest

# documentation
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  graphviz

%global _description %{expand:
The Modular toolkit for Data Processing (MDP) package is a library of
widely used data processing algorithms, and the possibility to combine
them together to form pipelines for building more complex data
processing software. MDP has been designed to be used as-is and as a
framework for scientific data processing development.

From the user’s perspective, MDP consists of a collection of units,
which process data. For example, these include algorithms for
supervised and unsupervised learning, principal and independent
components analysis and classification. These units can be chained
into data processing flows, to create pipelines as well as more
complex feed-forward network architectures. Given a set of input data,
MDP takes care of training and executing all nodes in the network in
the correct order and passing intermediate data between the nodes.
This allows the user to specify complex algorithms as a series of
simpler data processing steps.}

%description %_description

%package     -n python3-mdp
Summary:     %{summary}
Requires:    python3-future
Requires:    python3-numpy
Requires:    python3-scipy
Recommends:  python3-joblib
Recommends:  python3-scikit-learn
Recommends:  python3-pytest
Provides:    python3-bimdp = %{version}-%{release}
%{?python_provide:%python_provide python3-mdp}
%{?python_provide:%python_provide python3-bimdp}

%description -n python3-mdp %_description

%package     doc
Summary:     API documentation and tutorials for MDP
%description doc
%{summary}.

Also available online at http://mdp-toolkit.sourceforge.net.

%prep
%autosetup -n %extractdir -a1 -p1

%build
%py3_build
pushd mdp-docs-MDP-%{version}
ln -s .. mdp-toolkit
PYTHONPATH=.. make \
              MDPTOOLKIT=.. \
              SPHINXBUILD=sphinx-build-3 \
              LINKS=local \
              codesnippet html
rm build/html/.buildinfo

%install
%py3_install

%check
%{__python3} setup.py test -v

%global _docdir_fmt %{name}

%files -n python3-mdp
%{python3_sitelib}/*
%license COPYRIGHT

%files doc
%doc mdp-docs-MDP-%{version}/build/html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5-19
- Rebuilt for Python 3.9

* Thu Mar  5 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-18
- Update to git snapshot, fix build (#1793725)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5-16
- Rebuilt for Python 3.8

* Fri Aug  2 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-15
- Fix compatibility with sphinx-2.0 (#1736509)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5-13
- Subpackage python2-mdp has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-12
- Add patches to fix compatiblity with python3
- Use "python2-" prefixes to refer to python2 packages

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5-11
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-8
- Fix build with recent sphinx

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-6
- Backport upstream patches to fix build

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.5-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 10 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-3
- Run tests with fixed seed

* Wed Mar  9 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-2
- Disable failing test

* Tue Mar  8 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-1
- Initial packaging

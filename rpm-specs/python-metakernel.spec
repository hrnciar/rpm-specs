Name:		python-metakernel
#		The python and echo subpackages have their own version
#		and release numbers - update below in each package section
#		Running rpmdev-bumpspec on this specfile will update all the
#		release tags automatically
Version:	0.27.0
Release:	1%{?dist}
%global pkgversion %{version}
%global pkgrelease %{release}
Summary:	Metakernel for Jupyter

License:	BSD
URL:		https://github.com/Calysto/metakernel
Source0:	https://github.com/Calysto/metakernel/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-ipykernel
BuildRequires:	python3-pexpect >= 4.2
#		For testing:
BuildRequires:	python3-pytest
BuildRequires:	python3-requests
BuildRequires:	python3-ipyparallel
BuildRequires:	python3-jedi
BuildRequires:	man
#		For documentation
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx-bootstrap-theme
BuildRequires:	python3-numpydoc
BuildRequires:	python3-recommonmark

%description
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%package -n python3-metakernel
Summary:	Metakernel for Jupyter
%{?python_provide:%python_provide python3-metakernel}
Requires:	python3-ipykernel
Requires:	python3-pexpect >= 4.2
Obsoletes:	python3-metakernel-bash < 0.19.1-24

%description -n python3-metakernel
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%package -n python3-metakernel-tests
Summary:	Tests for python3-metakernel
%{?python_provide:%python_provide python3-metakernel-tests}
Requires:	python3-metakernel = %{version}-%{release}
Requires:	python3-metakernel-python
Requires:	python3-pytest
Requires:	python3-requests
Requires:	python3-ipyparallel
Requires:	python3-jedi
Requires:	man

%description -n python3-metakernel-tests
This package contains the tests of python3-metakernel.

%package doc
Summary:	Documentation for python-metakernel

%description doc
This package contains the documentation of python-metakernel.

%package -n python3-metakernel-python
Version:	0.19.1
Release:	36%{?dist}
Summary:	A Python kernel for Jupyter/IPython
%{?python_provide:%python_provide python3-metakernel-python}
Requires:	python3-metakernel = %{pkgversion}-%{pkgrelease}
Requires:	python3-jedi
Requires:	python-jupyter-filesystem

%description -n python3-metakernel-python
A Python kernel for Jupyter/IPython, based on MetaKernel.

%package -n python3-metakernel-echo
Version:	0.19.1
Release:	36%{?dist}
Summary:	A simple echo kernel for Jupyter/IPython
%{?python_provide:%python_provide python3-metakernel-echo}
Requires:	python3-metakernel = %{pkgversion}-%{pkgrelease}
Requires:	python-jupyter-filesystem

%description -n python3-metakernel-echo
A simple echo kernel for Jupyter/IPython, based on MetaKernel.

%prep
%setup -q -n metakernel-%{pkgversion}

%build
%py3_build

pushd metakernel_python
%py3_build
popd

pushd metakernel_echo
%py3_build
popd

pushd docs
PYTHONPATH=.. make html SPHINXBUILD=sphinx-build-3
rm -f _build/html/.buildinfo
popd

%install
%py3_install

pushd metakernel_python
%py3_install
popd

pushd metakernel_echo
%py3_install
popd

for f in tests/test_expect.py; do
  sed '/\/usr\/bin\/env/d' -i %{buildroot}%{python3_sitelib}/metakernel/${f}
done

PYTHONPATH=metakernel_python \
  python3 -m metakernel_python install --name python3-metakernel-python \
  --prefix %{buildroot}%{_prefix}
PYTHONPATH=metakernel_echo \
  python3 -m metakernel_echo install --name python3-metakernel-echo \
  --prefix %{buildroot}%{_prefix}

%check
PYTHONPATH=metakernel_python ipcluster start -n=3 &
pid=$!
pytest-3 -v metakernel
ipcluster stop
wait $pid

%files -n python3-metakernel
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/metakernel-*.egg-info
%dir %{python3_sitelib}/metakernel
%{python3_sitelib}/metakernel/*.py
%{python3_sitelib}/metakernel/__pycache__
%{python3_sitelib}/metakernel/images
%dir %{python3_sitelib}/metakernel/magics
%{python3_sitelib}/metakernel/magics/*.py
%{python3_sitelib}/metakernel/magics/__pycache__
%{python3_sitelib}/metakernel/utils

%files -n python3-metakernel-tests
%{python3_sitelib}/metakernel/tests
%{python3_sitelib}/metakernel/magics/tests

%files doc
%license LICENSE.txt
%doc docs/_build/html

%files -n python3-metakernel-python
%{python3_sitelib}/metakernel_python-*.egg-info
%{python3_sitelib}/metakernel_python.py
%{python3_sitelib}/__pycache__/metakernel_python.*
%{_datadir}/jupyter/kernels/python3-metakernel-python

%files -n python3-metakernel-echo
%{python3_sitelib}/metakernel_echo-*.egg-info
%{python3_sitelib}/metakernel_echo.py
%{python3_sitelib}/__pycache__/metakernel_echo.*
%{_datadir}/jupyter/kernels/python3-metakernel-echo

%changelog
* Thu Sep 03 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.27.0-1
- Update to version 0.27.0

* Wed Aug 26 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.26.1-1
- Update to version 0.26.1

* Sat Aug 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.26.0-1
- Update to version 0.26.0

* Wed Aug 19 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.25.1-1
- Update to version 0.25.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.24.4-2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.24.4-1
- Update to version 0.24.4
- Remove Python 2 parts from the spec file (Fedora 29 is EOL)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.24.3-1
- Update to version 0.24.3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.24.2-1
- Update to version 0.24.2
- Drop patch python-metakernel-Fix-TypeError.patch (accepted upstream)

* Wed Jun 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.24.1-1
- Update to version 0.24.1
- Drop metakernel-bash packages (upstream removed sources)
- Tests are now using pytest instead of nose
- Fix a TypeError

* Mon May 13 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.23.0-1
- Update to version 0.23.0

* Sun May 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.22.1-1
- Update to version 0.22.1

* Wed May 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.21.2-1
- Update to version 0.21.2

* Mon Apr 29 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.21.0-1
- Update to version 0.21.0
- Drop patch python-metakernel-adjustment-for-newer-jedi.patch (backported)
- Drop patch python-metakernel-python-exec.patch (accepted upstream)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-9
- Adapt to Python 3 only ipcluster in Fedora >= 30

* Tue Nov 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-8
- Don't build Python 2 packages for Fedora >= 30

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-7
- Don't rely on 'python' in path during testing

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-5
- Rebuilt for Python 3.7

* Mon Jun 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-4
- Adjustment for newer jedi (Backport from upstream git)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.20.14-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-1
- Update to 0.20.14
- Drop patches python-metakernel-install.patch and
  python-metakernel-bash-eval.patch (accepted upstream)
- Only provide one documentation package

* Sun Nov 26 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.12-2
- Use full path to python interpreter in kernel description
- Fix missing printout in bash kernel

* Fri Nov 17 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.12-1
- Update to 0.20.12

* Mon Oct 23 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.10-1
- Update to 0.20.10

* Fri Oct 20 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.8-1
- Update to 0.20.8

* Fri Sep 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.7-1
- Update to 0.20.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.4-1
- Update to 0.20.4

* Thu May 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.2-2
- Put tests in a separate subpackage

* Sat May 13 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.2-1
- Update to 0.20.2

* Sat Apr 29 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.1-1
- Initial packaging

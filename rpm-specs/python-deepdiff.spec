%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?fedora} >= 30
%bcond_with python2
%else
%bcond_without python2
%endif

# Don't have sphinx-sitemaps for now...
%bcond_with docs

Name:           python-deepdiff
Version:        5.0.2
Release:        1%{?dist}
Summary:        Deep Difference and search of any Python object/data
License:        MIT
URL:            https://github.com/seperman/deepdiff/
Source0:        https://github.com/seperman/deepdiff/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-ordered-set
BuildRequires:  python2-pytest
BuildRequires:  python2dist(jsonpickle)
BuildRequires:  python2dist(mock)
BuildRequires:  python2dist(setuptools)
# For docs
%if %{with docs}
BuildRequires:  python2dist(sphinx)
BuildRequires:  python2-dotenv
BuildRequires:  python2-sphinx-sitemap
%endif
# For tests
BuildRequires:  python2dist(numpy)
%endif
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-ordered-set
BuildRequires:  python3-pytest
BuildRequires:  python3dist(jsonpickle)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(setuptools)
# For docs
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-dotenv
BuildRequires:  python3-sphinx-sitemap
%endif
# For tests
BuildRequires:  python3dist(numpy)
%endif

%description
Deep Difference of dictionaries, iterables, strings and other
objects. It will recursively look for all the changes.

%if %{with python2}
%package     -n python2-deepdiff
Summary:        Python 2 package of %{name}
Requires:       python2-jsonpickle

%description -n python2-deepdiff
Deep Difference of dictionaries, iterables, strings and other
objects. It will recursively look for all the changes.

This is the Python 2 package.
%endif
# end with python2

%if %{with python3}
%package     -n python3-deepdiff
Summary:        Python 3 package of %{name}
Requires:       python3-jsonpickle

%description -n python3-deepdiff
Deep Difference of dictionaries, iterables, strings and other
objects. It will recursively look for all the changes.

This is the Python 3 package.
%endif 
# end with python3


%prep
%autosetup -n deepdiff-%{version}
find deepdiff/ -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' {} \;

%build
%if %{with python2}
%{py2_build}
%endif

%if %{with python3}
%{py3_build}
%endif
# end with python3

%if %{with docs}
# Build docs
make -C docs html
# remove the sphinx-build leftovers
rm -rf docs/_build/html/.{doctrees,buildinfo}
%endif

%install
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if %{with python3}
%{py3_install}
%endif 
# end with python3

%if %{with python2}
%{py2_install}
%endif
# end with python2

%check
%if %{with python3}
%{__python3} setup.py test
%endif
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python2}
%files -n python2-deepdiff
%license LICENSE
%doc AUTHORS README.md
%if %{with docs}
%doc docs/_build/html
%endif
%{python2_sitelib}/deepdiff/
%{python2_sitelib}/deepdiff-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-deepdiff
%license LICENSE
%doc AUTHORS README.md
%if %{with docs}
%doc docs/_build/html
%endif
%{python3_sitelib}/deepdiff/
%{python3_sitelib}/deepdiff-%{version}-py*.egg-info
%endif
# end with python3

%changelog
* Tue Aug 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.9

* Fri Mar 13 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.7-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.7-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.7-1
- Update to 4.0.7.

* Wed May 15 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.6-1
- Update to 4.0.6.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3.0-3
- Further review fixes.

* Mon Sep 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3.0-2
- Review fixes.

* Sat Sep 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3.0-1
- First release.


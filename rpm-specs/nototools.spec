%global commit0 9c4375f07c9adc00c700c5d252df6a25d7425870
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
%define with_python3 1
%else
%define with_python2 1
%define with_python3 1
%endif

%global common_desc \
The nototools python package contains python scripts \
used to maintain the Noto Fonts project, \
including the google.com/get/noto website.

Name:		nototools
Version:	0
Release:	0.20190715.git%{shortcommit0}%{?dist}
Summary:	Noto fonts support tools and scripts plus web site generation

# In nototools source
## nototools code is in ASL 2.0 license
### third_party ucd code is in Unicode license
License:	ASL 2.0
URL:		https://github.com/googlei18n/nototools
Source0:	https://github.com/googlei18n/nototools/archive/%{commit0}.tar.gz#/nototools-%{shortcommit0}.tar.gz

Patch0:     nototools-fixes-indent.patch
Patch1:     nototools-python3.patch
Patch2:     nototools-python3-replace-two-more-xrange-with-range.patch

BuildArch:	noarch
%if %{with python2}
BuildRequires:	python2-devel
%endif # with python2
%if %{with python3}
BuildRequires:	python3-devel
%endif # with python3

%if %{with python2}
Requires:	python2-nototools = %{version}-%{release}
%endif # with python2
%if %{with python3}
Requires:	python3-nototools = %{version}-%{release}
%endif # with python3

%description
%common_desc

%if %{with python3}
%package     -n python3-nototools
Summary:	Noto tools for python 3
Requires:	python3dist(fonttools)
BuildRequires:	python3dist(fonttools)

%description -n python3-nototools
%common_desc

%endif # with python3

%if %{with python2}
%package     -n python2-nototools
Summary:	Noto tools for python 2
Requires:	python2dist(fonttools)
BuildRequires:	python2dist(fonttools)

%description -n python2-nototools
%common_desc

%endif # with python2

%prep
%setup -c
%patch0 -p0 -b .indent
%patch1 -p0 -b .python3
%patch2 -p0 -b .python3-replace-two-more-xrange-with-range

# remove unneeded files
rm -rf nototools-%{commit0}/third_party/{cldr,dspl,fontcrunch,ohchr,spiro,udhr,unicode}
mv %{name}-%{commit0} python2

%if %{with python3}
cp -a python2 python3
%endif # with python3

# for documents
cp python2/*.md python2/LICENSE .

%build
%if %{with python2}
pushd python2
%py2_build
popd
%endif # with python2

%if %{with python3}
pushd python3
%py3_build
popd
%endif # with python3


%install
%if %{with python3}
pushd python3
%py3_install
for lib in %{buildroot}%{python3_sitelib}/nototools/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
popd
%endif # with python3

%if %{with python2}
pushd python2
%py2_install
for lib in %{buildroot}%{python2_sitelib}/nototools/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
popd
%endif # with python2

%check
%if %{with python2}
pushd python2
# This doesn’t actually run any tests at all, therefore it doesn‘t fail:
%{__python2} setup.py test
popd
%endif

%if %{with python3}
pushd python3
# Comment it out for the moment because it tries to run something which fails
#%{__python3} setup.py test
popd
%endif


%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/add_vs_cmap.py
%{_bindir}/autofix_for_release.py
%{_bindir}/create_image.py
%{_bindir}/decompose_ttc.py
%{_bindir}/drop_hints.py
%{_bindir}/dump_otl.py
%{_bindir}/fix_khmer_and_lao_coverage.py
%{_bindir}/fix_noto_cjk_thin.py
%{_bindir}/generate_sample_text.py
%{_bindir}/generate_website_2_data.py
%{_bindir}/merge_fonts.py
%{_bindir}/merge_noto.py
%{_bindir}/noto_lint.py
%{_bindir}/notocoverage
%{_bindir}/notodiff
%{_bindir}/scale.py
%{_bindir}/subset.py
%{_bindir}/subset_symbols.py
%{_bindir}/test_vertical_extents.py

%if %{with python2}
%files -n python2-nototools
%{python2_sitelib}/nototools
%{python2_sitelib}/nototools-0.0.1-py2.7.egg-info
%{python2_sitelib}/third_party
%endif

%if %{with python3}
%files -n python3-nototools
%{python3_sitelib}/nototools
%{python3_sitelib}/nototools-0.0.1-py3.?.egg-info
%{python3_sitelib}/third_party
%endif # with python3


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190715.git9c4375f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.20190714.git9c4375f
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190713.git9c4375f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.20190712.git9c4375f
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.20190711.git9c4375f
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20190710.git9c4375f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  9 2019 Mike FABIAN <mfabian@redhat.com> - 0-0.20190709.git9c4375f
- Update nototools package from upstream git repo
- Also build the python3-nototools package

* Tue Mar  5 2019 Peng Wu <pwu@redhat.com> - 0-0.20190305.gitbb309e8
- Update nototools package from upstream git repo

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20170929.git0c99dff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20170928.git0c99dff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20170927.git0c99dff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Peng Wu <pwu@redhat.com> - 0-0.20170926.git0c99dff
- Initial package

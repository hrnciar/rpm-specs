%global pkgname wxpython4
%global srcname wxPython
%bcond_without tests
%global sum New implementation of wxPython, a GUI toolkit for Python
%global desc \
wxPython4 is a is a new implementation of wxPython focused on improving speed,\
maintainability and extensibility. Just like "Classic" wxPython it wraps the\
wxWidgets C++ toolkit and provides access to the user interface portions of the\
wx API, enabling Python applications to have a GUI on Windows, Macs or Unix\
systems with a native look and feel and requiring very little (if any) platform\
specific code.

Name:           python-wxpython4
Version:        4.0.7
Release:        6%{?dist}
Summary:        %{sum}
# wxPython is licensed under the wxWidgets license.  The only exception is
# the pubsub code in wx/lib/pubsub which is BSD licensed.  Note: wxPython
# includes a bundled copy of wxWidgets in ext/wxWidgets which has a few
# bits of code that use other licenses.  This source is not used in the
# Fedora build, except for the interface headers in ext/wxWidgets/interface
# and the doxygen build scripts.
License:        wxWidgets and BSD
URL:            https://www.wxpython.org/
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
# wxPython upstream uses a private sip module, wx.siplib, and bundles the
# siplib code.  It's not possible to build this siplib because the source code
# for sipgen is not included.  Thus we unbundle sip and the sip package builds
# a wx.siplib for us in Fedora.
Patch0:         unbundle-sip.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  waf
BuildRequires:  wxGTK3-devel
# For tests
%if %{with tests}
BuildRequires:  glibc-langpack-en
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-wx-siplib
%endif

%description %{desc}

%package -n python3-%{pkgname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pkgname}}
BuildRequires:  python3-devel
BuildRequires:  python3-pathlib2
BuildRequires:  python3-pillow
BuildRequires:  python3-setuptools
BuildRequires:  python3-sip-devel >= 4.19.1
BuildRequires:  python3-six
Requires:       python3-pillow
Requires:       python3-wx-siplib-api(%{_sip_api_major})%{?_isa} >= %{_sip_api}
Requires:       python3-six

%description -n python3-%{pkgname} %{desc}

%package -n python3-%{pkgname}-media
Summary:        %{sum} (media module)
%{?python_provide:%python_provide python3-%{pkgname}-media}
Requires:       python3-%{pkgname}%{?_isa} = %{version}-%{release}

%description -n python3-%{pkgname}-media %{desc}
This package provides the wx.media module.

%package -n python3-%{pkgname}-webview
Summary:        %{sum} (webview module)
%{?python_provide:%python_provide python3-%{pkgname}-webview}
Requires:       python3-%{pkgname}%{?_isa} = %{version}-%{release}

%description -n python3-%{pkgname}-webview %{desc}
This package provides the wx.html2 module.

%package        doc
Summary:        Documentation and samples for wxPython
BuildArch:      noarch

%description doc
Documentation, samples and demo application for wxPython.


%prep
%autosetup -n %{srcname}-%{version} -p1

sed -i -e "s|WX_CONFIG = 'wx-config'|WX_CONFIG = 'wx-config-3.0'|" build.py
rm -rf sip/siplib
rm -rf wx/py/tests
rm -f docs/sphinx/_downloads/i18nwxapp/i18nwxapp.zip
cp -a wx/lib/pubsub/LICENSE_BSD_Simple.txt license
# Remove env shebangs from various files
sed -i -e '/^#!\//, 1d' demo/*.py{,w}
sed -i -e '/^#!\//, 1d' demo/agw/*.py
sed -i -e '/^#!\//, 1d' docs/sphinx/_downloads/i18nwxapp/*.py
sed -i -e '/^#!\//, 1d' samples/floatcanvas/*.py
sed -i -e '/^#!\//, 1d' samples/mainloop/*.py
sed -i -e '/^#!\//, 1d' samples/ribbon/*.py
sed -i -e '/^#!\//, 1d' wx/py/*.py
sed -i -e '/^#!\//, 1d' wx/tools/*.py
# Fix end of line encodings
sed -i 's/\r$//' docs/sphinx/_downloads/*.py
sed -i 's/\r$//' docs/sphinx/rest_substitutions/snippets/python/contrib/*.py
sed -i 's/\r$//' docs/sphinx/rest_substitutions/snippets/python/converted/*.py
sed -i 's/\r$//' docs/sphinx/_downloads/i18nwxapp/locale/I18Nwxapp.pot
sed -i 's/\r$//' docs/sphinx/make.bat
sed -i 's/\r$//' docs/sphinx/phoenix_theme/theme.conf
sed -i 's/\r$//' samples/floatcanvas/BouncingBall.py
# Remove spurious executable perms
chmod -x demo/*.py
chmod -x samples/mainloop/mainloop.py
chmod -x samples/printing/sample-text.txt
# Remove empty files
find demo -size 0 -delete
find docs/sphinx/rest_substitutions/snippets/python/converted -size 0 -delete
# Convert files to UTF-8
for file in demo/TestTable.txt docs/sphinx/_downloads/i18nwxapp/locale/I18Nwxapp.pot docs/sphinx/class_summary.pkl docs/sphinx/wx.1moduleindex.pkl; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done


%build
DOXYGEN=%{_bindir}/doxygen SIP=%{_bindir}/sip-wx WAF=%{_bindir}/waf %{__python3} -u build.py dox touch etg --nodoc sip build_py --use_syswx --gtk3


%install
%{__python3} build.py install_py --destdir=%{buildroot}
rm -f %{buildroot}%{_bindir}/*
# Remove locale files (they are provided by wxWidgets)
rm -rf %{buildroot}%{python3_sitearch}/wx/locale

%check
%if %{with tests}
SKIP_TESTS="'not (display_Tests or glcanvas_Tests or mousemanager_Tests or numdlg_Tests or uiaction_MouseTests or uiaction_KeyboardTests or unichar_Tests or valtext_Tests or test_frameRestore or test_grid_pi)'"
ln -sf %{python3_sitearch}/wx/siplib.so wx/siplib.so
xvfb-run -a %{__python3} build.py test --pytest_timeout=60 --extra_pytest="-k $SKIP_TESTS" --verbose || true
%endif


%files -n python3-%{pkgname}
%license license/*
%{python3_sitearch}/*
%exclude %{python3_sitearch}/wx/*html2*
%exclude %{python3_sitearch}/wx/__pycache__/*html2*
%exclude %{python3_sitearch}/wx/*media*
%exclude %{python3_sitearch}/wx/__pycache__/*media*

%files -n python3-%{pkgname}-media
%{python3_sitearch}/wx/*media*
%{python3_sitearch}/wx/__pycache__/*media*

%files -n python3-%{pkgname}-webview
%{python3_sitearch}/wx/*html2*
%{python3_sitearch}/wx/__pycache__/*html2*

%files doc
%doc docs demo samples
%license license/*


%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.7-6
- Rebuilt for Python 3.9

* Mon Feb 10 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.7-5
- Rebuilt to fix an undefined symbol (#1801244)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Scott Talbert <swt@techie.net> - 4.0.7-3
- Build using unbundled copy of waf (#1789646)

* Thu Nov 07 2019 Scott Talbert <swt@techie.net> - 4.0.7-2
- Remove BR on python-PyPDF2 - PDF tests are disabled by default anyway

* Sat Oct 26 2019 Scott Talbert <swt@techie.net> - 4.0.7-1
- Update to new upstream release 4.0.7 (#1765757)

* Mon Sep 16 2019 Scott Talbert <swt@techie.net> - 4.0.6-9
- Remove Python 2 subpackages (#1629793)

* Thu Aug 29 2019 Scott Talbert <swt@techie.net> - 4.0.6-8
- Switch to using private sip module, wx.siplib (#1739469)

* Wed Aug 28 2019 Scott Talbert <swt@techie.net> - 4.0.6-7
- Fix FloatCanvas with Python 3.8 (time.clock removed)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.6-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 25 2019 Scott Talbert <swt@techie.net> - 4.0.6-4
- Stop running tests for Python 2 to release some Py2 dependencies

* Wed Jul 17 2019 Scott Talbert <swt@techie.net> - 4.0.6-3
- Fix FTBFS due to easy_install switch to Python 3

* Fri Jun 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.0.6-2
- >= sip-api

* Tue May 21 2019 Scott Talbert <swt@techie.net> - 4.0.6-1
- Update to new upstream release 4.0.6 (#1711733)

* Sat May 18 2019 Scott Talbert <swt@techie.net> - 4.0.4-4
- Fix FTBFS with Python 3.8 (#1710767)

* Sat Apr 06 2019 Scott Talbert <swt@techie.net> - 4.0.4-3
- Fix FTBFS with SIP 4.19.14 (#1696302)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Scott Talbert <swt@techie.net> - 4.0.4-1
- New upstream release 4.0.4

* Tue Nov 20 2018 Scott Talbert <swt@techie.net> - 4.0.1-11
- Fix tests

* Sat Oct 27 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.1-10
- Rebuilt for sip update

* Mon Jul 16 2018 Scott Talbert <swt@techie.net> - 4.0.1-9
- Replace use of python3-sip binary with sip (fixes FTBFS)
- Use sip-api macros to ensure dependency on correct sip module version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Scott Talbert <swt@techie.net> - 4.0.1-7
- Re-enable tests but enable pytest-timeout

* Wed Jun 20 2018 Scott Talbert <swt@techie.net> - 4.0.1-6
- Cherry-pick waf 2.0.7 updates to fix Python 3.7 FTBFS (#1593029)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-5
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Scott Talbert <swt@techie.net> - 4.0.1-4
- Add missing BR for gcc-c++

* Thu Feb 15 2018 Scott Talbert <swt@techie.net> - 4.0.1-3
- Second round of review comment fixes

* Tue Feb 13 2018 Scott Talbert <swt@techie.net> - 4.0.1-2
- Address initial review comments
- Fix rpmlint errors
- Fix and enable tests (but they are still not required to pass)

* Wed Feb 07 2018 Scott Talbert <swt@techie.net> - 4.0.1-1
- Initial packaging

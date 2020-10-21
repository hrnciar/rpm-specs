%global sum Image Viewer and Toolkit
%global common_desc                                                           \
Ginga is a toolkit designed for building viewers for scientific image data in \
Python, visualizing 2D pixel data in numpy arrays. It can view astronomical   \
data such as contained in files based on the FITS (Flexible Image Transport   \
System) file format. It is written and is maintained by software engineers at \
the Subaru Telescope, National Astronomical Observatory of Japan.             \
                                                                              \
The Ginga toolkit centers around an image display class which supports zooming\
and panning, color and intensity mapping, a choice of several automatic cut   \
levels algorithms and canvases for plotting scalable geometric forms. In      \
addition to this widget, a general purpose “reference” FITS viewer is         \
provided, based on a plugin framework. A fairly complete set of standard      \
plugins are provided for features that we expect from a modern FITS viewer:   \
panning and zooming windows, star catalog access, cuts, star pick/fwhm,       \
thumbnails, etc.

Name:           ginga
Version:        2.7.2
Release:        8%{?dist}
Summary:        %{sum}
# License breakdown
#
# In general (if not listed below): BSD
#
# Apache 2.0
#   astropy_helpers/astropy_helpers/sphinx/themes/bootstrap-astropy/static/bootstrap-astropy.css
#   ginga/util/heaptimer.py
# 
# MIT/X11
#   ginga/util/six.py
#
License:        BSD and ASL 2.0 and MIT
URL:            https://ejeschke.github.io/ginga/
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz

# General build reqs
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
BuildRequires:  google-roboto-fonts
# Python 3 build reqs
BuildRequires:  python3-astropy
BuildRequires:  python3-astropy-helpers
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib-qt5
BuildRequires:  python3-piexif
BuildRequires:  python3-pillow
BuildRequires:  python3-opencv
BuildRequires:  python3-QtPy
BuildRequires:  python3-qt5
BuildRequires:  python3-scipy

Requires:       python3-%{name} = %{version}-%{release}

BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{name}}
Requires:       google-roboto-fonts
Requires:       python3-astropy
Requires:       python3-beautifulsoup4
Requires:       python3-matplotlib-qt5
Requires:       python3-opencv
Requires:       python3-piexif
Requires:       python3-pillow
Requires:       python3-QtPy
Requires:       python3-qt5
Requires:       python3-scipy

%description -n python3-%{name}
%{common_desc}

%package -n python3-%{name}-examples
Summary:        Examples for %{name}
%{?python_provide:%python_provide python3-%{name}-examples}
Requires:       python3-%{name} = %{version}-%{release}

%description -n python3-%{name}-examples
Examples for %{name}


%prep
%autosetup
cp -r ginga/examples examples-py3
# Fix wrong Python interpreters (upstream uses env)
find examples-py3 -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'

%build
%py3_build

%install
%py3_install
desktop-file-install                                    \
     --dir=%{buildroot}%{_datadir}/applications         \
     %{name}.desktop

# Replace bundled fonts with symlinks to system fonts
rm -f %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/*
ln -sf %{_fontbasedir}/google-roboto/Roboto-Black.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Black.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Bold.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Bold.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Light.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Light.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Medium.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Medium.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Regular.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Regular.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Thin.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Thin.ttf

# ginga/web/pgw/ipg.py has wrong permissions
chmod 755 %{buildroot}/%{python3_sitelib}/%{name}/web/pgw/ipg.py
chmod 755 %{buildroot}/%{python3_sitelib}/%{name}/util/mosaic.py

# Fix wrong interpreters in some scripts...
find %{buildroot}/%{python3_sitelib}/%{name} -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'


%files
%license LICENSE.txt
%doc README.txt
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop

%files -n python3-%{name}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/*
# Examples are shipped as documentation in examples subpackage
%exclude %{python3_sitelib}/%{name}/examples

%files -n python3-%{name}-examples
%license LICENSE.txt
%doc examples-py3/*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.2-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.2-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 2.7.2-1
- new version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.7.1-2
- drop python2 subpackage (#1632317)

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.7.1-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.5-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.5-2
- Remove obsolete scriptlets

* Fri Sep 08 2017 Christian Dersch <lupinix@mailbox.org> - 2.6.5-1
- new version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Christian Dersch <lupinix@mailbox.org> - 2.6.2-2
- Added dependency python-QtPy

* Tue Feb 28 2017 Christian Dersch <lupinix@mailbox.org> - 2.6.2-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Christian Dersch <lupinix@mailbox.org> - 2.6.1-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Christian Dersch <lupinix@mailbox.org> - 2.6.0-1
- new version

* Sat Oct 22 2016 Christian Dersch <lupinix@mailbox.org> - 2.5.20161005204600-1
- new version
- unbundled fonts
- fixed interpreters for scripts to use correct Python version

* Sun Oct  2 2016 Christian Dersch <lupinix@mailbox.org> - 2.5.20160926130800-1
- initial package

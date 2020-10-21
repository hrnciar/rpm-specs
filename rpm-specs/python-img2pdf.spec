%global         srcname  img2pdf
%global         desc   Python 3 library and command line utility img2pdf for losslessly converting\
a bunch of image files into a PDF file. That means that the images\
are either inserted into the PDF as-is or they are recompressed using\
lossless compression. Thus, img2pdf usually runs faster and may yield\
smaller PDF files than an ImageMagick convert command.\
\
The img2pdf command complements the pdfimages command.

Name:           python-%{srcname}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Lossless images to PDF conversion library and command

License:        LGPLv3+
URL:            https://pypi.org/project/img2pdf
Source0:        %pypi_source

# https://sources.debian.org/data/main/i/img2pdf/0.4.0-1/debian/patches/imdepth.patch
Patch0:         imdepth.patch
# XXX TODO remove when upstream
Patch1:         test-byteorder.diff

BuildArch:      noarch

# cf. Bug 1851638 - img2pdf fails to build on s390x because of issues in the ImageMagick dependency
# https://bugzilla.redhat.com/show_bug.cgi?id=1851638
ExcludeArch:    s390x

# required for tests
BuildRequires:  python3-pytest
BuildRequires:  ImageMagick
BuildRequires:  ghostscript
BuildRequires:  libtiff-tools
BuildRequires:  mupdf
BuildRequires:  netpbm-progs
BuildRequires:  perl-Image-ExifTool
BuildRequires:  poppler-utils
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy

# other requirements
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


BuildRequires:  python3-pillow
# TODO will be removed in some future img2pdf release
# cf. https://gitlab.mister-muffin.de/josch/img2pdf/issues/74#note_1037
BuildRequires:  python3-pdfrw
BuildRequires:  python3-pikepdf

# this is basically equivalent to adding Requires: for
# pikepdf
# pillow
%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
sed -i '1{/^#!\//d}' src/*.py
%py3_build

%install
%py3_install

%check

# since the test directly calls src/img2pdf.py
# (file is already installed at this point)
sed -i '1i#!'%{__python3} src/img2pdf.py

# XXX TODO in next release
sed -i 's/assert identify\[0\]\["image"\]\.get("endianess")/assert get_byteorder(identify)/' src/img2pdf_test.py
# XXX TODO remove -k in next release
# cf. https://gitlab.mister-muffin.de/josch/img2pdf/issues/85
PYTHONPATH=src %{__python3} -m pytest src/img2pdf_test.py -k 'not test_png_icc and not test_tiff_ccitt_nometa2'

%files -n python3-%{srcname}
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-gui
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/jp2.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{srcname}-%{version}*.egg-info
%doc README.md


%changelog
* Sun Sep 20 2020 Georg Sauthoff <mail@gms.tf> - 0.4.0-1
- Update to latest upstream version (fixes fedora#1867007)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Georg Sauthoff <mail@gms.tf> - 0.3.4-5
- Temporarily disable some tests until next release fixes them.

* Fri Jun 26 2020 Georg Sauthoff <mail@gms.tf> - 0.3.4-4
- Be more explicit regarding setuptools depenency,
  cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-3
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Georg Sauthoff <mail@gms.tf> - 0.3.4-2
- Add upstream fix for test suite failure on aarch64

* Sun Apr 26 2020 Georg Sauthoff <mail@gms.tf> - 0.3.4-1
- Update to latest upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Georg Sauthoff <mail@gms.tf> - 0.3.2-2
- Fix unittest false-negatives on aarch64
* Sat Nov 24 2018 Georg Sauthoff <mail@gms.tf> - 0.3.2-1
- Update to latest upstream version
* Sat Aug 11 2018 Georg Sauthoff <mail@gms.tf> - 0.3.1-1
- Update to latest upstream version
* Wed Aug 1 2018 Georg Sauthoff <mail@gms.tf> - 0.3.0-1
- Update to latest upstream version
* Tue May 1 2018 Georg Sauthoff <mail@gms.tf> - 0.2.4-1
- initial packaging

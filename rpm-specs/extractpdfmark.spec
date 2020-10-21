Name:           extractpdfmark
Version:        1.1.0
Release:        6%{?dist}
Summary:        Extract page mode and named destinations as PDFmark from PDF

License:        GPLv3+
URL:            https://github.com/trueroad/extractpdfmark/
Source0:        https://github.com/trueroad/extractpdfmark/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  poppler-cpp-devel

%description
When you create a PDF document using something like a TeX system you may include
many small PDF files in the main PDF file. It is common for each of the small
PDF files to use the same fonts.

If the small PDF files contain embedded font subsets, the TeX system includes
them as-is in the main PDF. As a result, several subsets of the same font are
embedded in the main PDF. It is not possible to remove the duplicates since they
are different subsets. This vastly increases the size of the main PDF file.

On the other hand, if the small PDF files contain embedded full font sets, the
TeX system also includes all of them in the main PDF. This time, the main PDF
contains duplicates of the same full sets of fonts. Therefore, Ghostscript can
remove the duplicates. This may considerably reduce the main PDF-file's size.

Finally, if the small PDF files contain some fonts that are not embedded, the
TeX system outputs the main PDF file with some fonts missing. In this case,
Ghostscript can embed the necessary fonts. It can significantly reduce the
required disk size.

Either way, when Ghostscript reads the main PDF produced by the TeX system and
outputs the final PDF it does not preserve PDF page-mode and named-destinations
etc. As a result, when you open the final PDF, it is not displayed correctly.
Also, remote PDF links will not work correctly.

This program is able to extract page mode and named destinations as PDFmark from
PDF. By using this you can get the small PDF files that have preserved them.

%prep
%autosetup -p1


%build
%configure --with-poppler=cpp
%make_build


%install
%make_install
rm %{buildroot}%{_pkgdocdir}/COPYING

%check
make check

%files
%{_mandir}/man1/extractpdfmark.1.*
%{_bindir}/extractpdfmark

%license COPYING

%doc NEWS README.*



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Marek Kasik <mkasik@redhat.com> - 1.1.0-5
- Use stable cpp front-end of poppler

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 1.1.0-3
- Rebuild for poppler-0.84.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Federico Bruni <fede@inventati.org> - 1.1.0-1
- Upgrade to version 1.1.0

* Mon Jul 1 2019 Federico Bruni <fede@inventati.org> - 1.0.3-1
- Upgrade to version 1.0.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Marek Kasik <mkasik@redhat.com> - 1.0.2-6
- Rebuild for poppler-0.73.0

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 1.0.2-5
- Rebuild for poppler-0.67.0

* Mon Jul 16 2018 Federico Bruni <fede@inventati.org> - 1.0.2-4
- Add gcc-c++ build requirement

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Federico Bruni <fede@inventati.org> - 1.0.2-2
- Fix issues mentioned in review: https://bugzilla.redhat.com/show_bug.cgi?id=1520922

* Mon Nov  6 2017 Federico Bruni <fede@inventati.org> - 1.0.2-1
- Release 1.0.2


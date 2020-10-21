%global packname prettydoc
%global packver  0.4.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Creating Pretty Documents from R Markdown

License:          ASL 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-rmarkdown >= 1.17
# Suggests:  R-knitr, R-KernSmooth
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         open-sans-fonts
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    open-sans-fonts
BuildRequires:    R-rmarkdown >= 1.17
BuildRequires:    R-knitr
BuildRequires:    R-KernSmooth

%description
Creating tiny yet beautiful documents and vignettes from R Markdown. The
package provides the 'html_pretty' output format as an alternative to the
'html_document' and 'html_vignette' engines that convert R Markdown into
HTML pages. Various themes and syntax highlight styles are supported.


%prep
%setup -q -c -n %{packname}

# Switch font names to system names.
pushd %{packname}/inst/resources/css
sed -i -e 's/open-sans-700.woff/OpenSans-Bold.ttf/g' *.css
sed -i -e 's/open-sans-400.woff/OpenSans-Regular.ttf/g' *.css
sed -i -e "s/format('woff');/format('ttf');/g" -e 's/format("woff");/format("ttf");/g' *.css
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{rlibdir}/%{packname}/resources/fonts
rm open-sans-400.woff open-sans-700.woff
ln -s /usr/share/fonts/open-sans/OpenSans-Regular.ttf
ln -s /usr/share/fonts/open-sans/OpenSans-Bold.ttf
popd


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/resources
%{rlibdir}/%{packname}/rmarkdown


%changelog
* Tue Aug 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version (rhbz#1867788)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.1-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-3
- Fix unbundling of fonts

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- initial package for Fedora

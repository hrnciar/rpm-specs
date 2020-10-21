%global packname crosstalk
%global packver  1.1.0.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.1.0.1
Release:          1%{?dist}
Summary:          Inter-Widget Interactivity for HTML Widgets

# Mostly MIT, selectize.js is ASL 2.0
License:          MIT and ASL 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# Remove extra glyphicons references; Fedora only;
Patch0001:        0001-Remove-non-ttf-font-references.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-htmltools >= 0.3.5, R-jsonlite, R-lazyeval, R-R6
# Suggests:  R-shiny, R-ggplot2, R-testthat >= 2.1.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-htmltools >= 0.3.5
BuildRequires:    R-jsonlite
BuildRequires:    R-lazyeval
BuildRequires:    R-R6
BuildRequires:    R-shiny >= 0.11
BuildRequires:    R-ggplot2
BuildRequires:    R-testthat >= 2.1.0

BuildRequires: web-assets-devel
# MIT; inst/lib/bootstrap/
# https://github.com/twbs/bootstrap/releases/tag/v3.4.1
Provides:         bundled(xstatic-bootstrap-common) = 3.4.1
BuildRequires:    glyphicons-halflings-fonts
Requires:         glyphicons-halflings-fonts

# MIT; inst/lib/ionrangeslider
Provides:         bundled(js-IonDen-ionrangeslider) = 2.1.2

# MIT; inst/lib/jquery
BuildRequires:    js-jquery3 >= 3.4.1
Requires:         js-jquery3 >= 3.4.1

# ASL 2.0; inst/lib/selectize
Provides:         bundled(js-brianreavis-selectize) = 0.12.1

# MIT; inst/lib/strftime
Provides:         bundled(js-samsonjs-strftime) = 0.9.2

%description
Provides building blocks for allowing HTML widgets to communicate with each
other, with Shiny or without (i.e. static .html files). Currently supports
linked brushing and filtering.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

pushd %{buildroot}%{rlibdir}/%{packname}
# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
ln -sf %{_datadir}/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf \
    lib/bootstrap/fonts/glyphicons-halflings-regular.ttf

for f in jquery.js jquery.min.js jquery.min.map; do
    ln -sf %{_jsdir}/jquery/3/$f lib/jquery/$f
done
popd


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/lib
%{rlibdir}/%{packname}/www


%changelog
* Sun Aug 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0.1-1
- initial package for Fedora

# Generated by go2rpm
%bcond_without check

# https://github.com/ajstarks/deck
%global goipath         github.com/ajstarks/deck
%global commit          b22ec51b2c1e28a2cdaf016c16a22456e10188df

%gometa

%global common_description %{expand:
Deck is a library for clients to make scalable presentations, using a standard
markup language. Clients read deck files into the Deck structure, and traverse
the structure for display, publication, etc. Clients may be interactive or
produce standard formats such as SVG or PDF.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Slide Decks

License:        CC-BY
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/ajstarks/svgo)
BuildRequires:  golang(github.com/ajstarks/svgo/float)
BuildRequires:  golang(github.com/disintegration/gift)
BuildRequires:  golang(github.com/fogleman/gg)
BuildRequires:  golang(github.com/jung-kurt/gofpdf)

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf cmd/vgdeck

%build
for cmd in cmd/pngdeck cmd/pdfdeck cmd/svgdeck ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc examples README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 18:09:25 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20200126gitb22ec51
- Bump to commit b22ec51b2c1e28a2cdaf016c16a22456e10188df

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 22:51:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701git3beea55
- Initial package

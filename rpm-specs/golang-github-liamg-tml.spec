# Generated by go2rpm 1
%bcond_without check

# https://github.com/liamg/tml
%global goipath         github.com/liamg/tml
Version:                0.3.0

%gometa

%global common_description %{expand:
A Go module (and standalone binary) to make the output of
colored/formatted text in the terminal easier and more
readable.}

%global golicenses      LICENSE
%global godocs          _examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Markup language for terminal output

License:        Unlicense
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in tml; do
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
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Oct 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-2
- Ship the examples only in the -devel package (#1882895)

* Sat Sep 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package
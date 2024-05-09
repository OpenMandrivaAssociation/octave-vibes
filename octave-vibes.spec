%global octpkg vibes

Summary:	Integrates the VIBes API into Octave
Name:		octave-vibes
Version:	0.2.0
Release:	3
License:	GPLv3+ and MIT
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/vibes/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?58859
Patch0:		octave5.patch
# https://savannah.gnu.org/bugs/index.php?59376
Patch1:		build-against-octave-6.patch

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	octave-interval

Requires:	octave(api) = %{octave_api}
Requires:	octave-interval

Requires(post): octave
Requires(postun): octave

%description
The VIBes API allows one to easily display results (boxes, pavings) from
interval methods. VIBes consists in two parts:
 
 1. the VIBes application that features viewing, annotating and exporting
    figures;
 2. the VIBes API that enables your program to communicate with the viewer
    in order to draw figures.
 
This package integrates the VIBes API into Octave. The VIBes application
is required for operation and must be installed seperately. Data types from
third-party interval arithmetic libraries for Octave are also supported.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild


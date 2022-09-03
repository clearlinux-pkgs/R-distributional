#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-distributional
Version  : 0.3.1
Release  : 7
URL      : https://cran.r-project.org/src/contrib/distributional_0.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/distributional_0.3.1.tar.gz
Summary  : Vectorised Probability Distributions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-digest
Requires: R-farver
Requires: R-generics
Requires: R-ggplot2
Requires: R-lifecycle
Requires: R-numDeriv
Requires: R-rlang
Requires: R-scales
Requires: R-vctrs
BuildRequires : R-digest
BuildRequires : R-farver
BuildRequires : R-generics
BuildRequires : R-ggplot2
BuildRequires : R-lifecycle
BuildRequires : R-numDeriv
BuildRequires : R-rlang
BuildRequires : R-scales
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
visualising, and using probability distributions. Designed to allow model
    prediction outputs to return distributions rather than their parameters, 
    allowing users to directly interact with predictive distributions in a
    data-oriented workflow. In addition to providing generic replacements for
    p/d/q/r functions, other useful statistics can be computed including means,
    variances, intervals, and highest density regions.

%prep
%setup -q -n distributional
cd %{_builddir}/distributional

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662137616

%install
export SOURCE_DATE_EPOCH=1662137616
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/distributional/DESCRIPTION
/usr/lib64/R/library/distributional/INDEX
/usr/lib64/R/library/distributional/Meta/Rd.rds
/usr/lib64/R/library/distributional/Meta/features.rds
/usr/lib64/R/library/distributional/Meta/hsearch.rds
/usr/lib64/R/library/distributional/Meta/links.rds
/usr/lib64/R/library/distributional/Meta/nsInfo.rds
/usr/lib64/R/library/distributional/Meta/package.rds
/usr/lib64/R/library/distributional/NAMESPACE
/usr/lib64/R/library/distributional/NEWS.md
/usr/lib64/R/library/distributional/R/distributional
/usr/lib64/R/library/distributional/R/distributional.rdb
/usr/lib64/R/library/distributional/R/distributional.rdx
/usr/lib64/R/library/distributional/help/AnIndex
/usr/lib64/R/library/distributional/help/aliases.rds
/usr/lib64/R/library/distributional/help/distributional.rdb
/usr/lib64/R/library/distributional/help/distributional.rdx
/usr/lib64/R/library/distributional/help/figures/README-plot-1.png
/usr/lib64/R/library/distributional/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/distributional/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/distributional/help/paths.rds
/usr/lib64/R/library/distributional/html/00Index.html
/usr/lib64/R/library/distributional/html/R.css
/usr/lib64/R/library/distributional/tests/testthat.R
/usr/lib64/R/library/distributional/tests/testthat/Rplots.pdf
/usr/lib64/R/library/distributional/tests/testthat/setup-tests.R
/usr/lib64/R/library/distributional/tests/testthat/test-apply.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-bernoulli.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-beta.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-burr.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-cauchy.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-chisq.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-degenerate.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-exponential.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-f.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-gamma.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-geometric.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-gumbel.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-hypergeometric.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-inverse-exponential.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-inverse-gamma.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-inverse-gaussian.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-logarithmic.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-logistic.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-multinomial.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-multivariate-normal.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-negative-binomial.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-normal.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-pareto.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-percentile.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-poisson-inverse-gaussian.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-sample.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-student-t.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-studentised-range.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-uniform.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist-weibull.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist_categorical.R
/usr/lib64/R/library/distributional/tests/testthat/test-dist_lognormal.R
/usr/lib64/R/library/distributional/tests/testthat/test-distribution.R
/usr/lib64/R/library/distributional/tests/testthat/test-graphics.R
/usr/lib64/R/library/distributional/tests/testthat/test-hilo.R
/usr/lib64/R/library/distributional/tests/testthat/test-inflated.R
/usr/lib64/R/library/distributional/tests/testthat/test-issues.R
/usr/lib64/R/library/distributional/tests/testthat/test-mixture.R
/usr/lib64/R/library/distributional/tests/testthat/test-transformations.R
/usr/lib64/R/library/distributional/tests/testthat/test-truncated.R
